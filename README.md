# wazuh-sigma-rules

A custom Wazuh 4.14 detection ruleset converted to [Sigma](https://sigmahq.io). It covers web attacks against nginx and Linux host activity (sudo, sshd, file integrity), mapped to MITRE ATT&CK.

| Directory | Count | Content |
|---|---|---|
| `rules/web/` | 168 | nginx access-log detections in 22 attack classes (SQLi, XSS, SSRF, path traversal, upload, web shell, ...), plus an "attack pattern returned HTTP 200" rule per class |
| `rules/linux/` | 132 | sudo command-line, sshd and file-integrity detections, grouped by ATT&CK tactic (one is a correlation base rule) |
| `rules/correlations/` | 32 | Sigma correlation rules: repeat counts per source IP / user, and multi-technique bursts per tactic |
| `filters/` | 5 | Sigma filters for false positives that apply anywhere (static assets, UUIDs, TLS bytes on a plain port, ...) |
| `pipelines/wazuh.yml` | | pySigma pipeline: Sigma taxonomy fields to Wazuh alert fields |
| `tests/` | 62 cases | Web replay cases, with the rule names each case must fire after filters |
| `CONVERSION.md` | 516 | Every source Wazuh rule ID and where it went |

All rules are `status: experimental`. Each rule keeps its source Wazuh rule ID(s) in `wazuh_rule_id`, and its `id` is a UUIDv5 of `wazuh:<rule id>`, so conversions are reproducible.

## Use

```bash
pip install sigma-cli pySigma-backend-opensearch
sigma check rules && sigma check filters
sigma convert -t opensearch_lucene -p pipelines/wazuh.yml --filter filters rules/web
python3 tests/run_tests.py          # needs: pip install pyyaml regex
```

Correlations live under `rules/` because sigma-cli resolves a correlation's `rules:` only within one input path. For a backend other than Wazuh/OpenSearch, drop `-p pipelines/wazuh.yml` and use that backend's own pipeline. The rules use standard Sigma taxonomy fields.

## Field mapping (`pipelines/wazuh.yml`)

The web rules were written for two nginx log formats that Wazuh decodes differently. Each taxonomy field maps to both, and the backend ORs them.

| Sigma field | Plaintext access log (`web-accesslog`) | JSON access log (`json`) |
|---|---|---|
| `cs-uri-query` (full request URI) | `data.url` | `data.requesturi` |
| `sc-status` | `data.id` | `data.code` |
| `c-ip` | `data.srcip` | `data.remote` |
| `cs-method` | `data.protocol` | `data.method` |
| `cs-user-agent` | `data.agent` | `data.agent` |
| `cs-host` | `data.servername` | `data.servername` |

Linux mappings:

| Rule logsource | Sigma field | Wazuh field |
|---|---|---|
| `service: sudo` | `CommandLine` | `full_log` |
| `service: sudo` | `User` | `data.srcuser` |
| `service: sshd` | `Message` | `full_log` |
| `service: sshd` | `c-ip` | `data.srcip` |
| `service: sshd` | `User` | `data.dstuser` |
| `category: file_event` | `TargetFilename` | `syscheck.path` |
| `category: file_event` | `User` | `syscheck.uname_after` |

`cs-uri-query` holds the whole request URI (path and query), following the SigmaHQ webserver rules.

## Caveats

- **The regexes are PCRE and need a PCRE-capable engine.** OpenSearch/Lucene `regexp` has no `^`/`$` anchors (the pattern must match the whole value), no `\b`, `\s` or `\d`, no lookarounds, and no documented `(?i)` ([OpenSearch regex syntax](https://docs.opensearch.org/latest/query-dsl/regex-syntax/)). `opensearch_lucene` output is syntactically valid, but it will not match the same events the rules describe. Use a backend with PCRE/Java regex, or rewrite the patterns for Lucene.
- **Wazuh indexes alerts, not raw events.** A query-time deployment over `wazuh-alerts-*` only sees events that already matched some Wazuh rule at or above the alert level. Index archives or ship the raw logs to run these rules as primary detections.
- **Correlation rules need a backend that supports them.** In pySigma-backend-opensearch only the PPL backend (`open_search_ppl`, pre-release) implements them. In version 2.0.3 it fails on this set ("Conversion result not available") whenever two rules in the collection share an identical selection item. A single correlation together with its base rule converts fine. pySigma does not apply filters to correlation rules.
- **`group-by` fields are not mapped by the pipeline.** `c-ip` maps to two Wazuh fields (one per log format), and a correlation can only group by one field. Map `c-ip` / `User` to your backend's single source-IP / user field before converting correlations.
- Wazuh "lowers to level 3" was converted to a filter that suppresses outright. At level 3 these events were already below every alerting threshold.

## Intentional changes from the source rules

- **No status gate on pattern rules.** The JSON-stream rules required `status ∈ {200,401,403,500,502,503}`, while the plaintext twins had dropped that gate. The ungated form was kept, and each attack class has a separate HTTP-200 rule for "the server processed it". Gates that are part of a rule's meaning stay: 401/403 for failed logins, 429 for rate limiting, 5xx for server errors, 200 for IDOR access.
- **Twins with different regexes:** the false-positive-fixed variant was kept. This covers `rO0ABX|aced0005` without the bare `AAAAAA` branch, `Spring[0-9]` as a whole token, the encoded-whitespace OR-injection form, and the encoded `<!DOCTYPE`/`<?xml` forms.
- **CSRF POST to sensitive endpoint** keeps the POST method gate (one source variant had none).
- **Failed API authentication** counts 401/403 only (429 is a rate limit, not an auth failure).
- **Known scanner User-Agent** matches `cs-user-agent`, not the whole log line.
- **HTTP-200 rules** leave out source rules whose own status gate excludes 200, since those could never chain in Wazuh either.
- **ATT&CK v19 renumbering:** T1562 → T1685 (Disable or Modify Tools), T1562.001 audit → T1685.004, T1562.004 → T1686 (Disable or Modify System Firewall), T1070.002 → T1685.006. Tactic tags follow the current technique-to-tactic mapping, including `stealth` and `defense-impairment`, which replace `defense-evasion`.
- Rules that could never match in Wazuh, tuning of Wazuh built-in rules, and site-specific exclusions were not converted. `CONVERSION.md` gives the reason for each.

## Validation

- `sigma check`: 0 errors, 0 issues, using pySigma's ATT&CK v19.2 data.
- Every detection rule converts with `opensearch_lucene` and `pipelines/wazuh.yml`, with the filters applied. Correlation references resolve (`sigma check`).
- **Equivalence replay.** Each web rule and its source Wazuh rule(s) were evaluated over about 1,500 production URLs × 9 status codes × 2 methods (28k events). 162 of 167 rules agree on every event. The 5 that differ are the intentional changes listed above. The production corpus is not published.
- `tests/run_tests.py`: 62 sanitized cases (attack positives, near-miss negatives, and a kept/suppressed pair per filter), with expectations cross-checked against the Wazuh source rules.

## License

[Detection Rule License (DRL) 1.1](LICENSE.Detection.Rules.md).
