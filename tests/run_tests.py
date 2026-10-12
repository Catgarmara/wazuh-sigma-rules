#!/usr/bin/env python3
"""Replay tests/web_cases.tsv through the web rules and filters with tools/sigma_eval.py.
Each case lists the Sigma rule names that must fire after filters ('-' = none). Exit 1 on any mismatch."""
import glob, os, sys
import yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from sigma_eval import rule_matches, filter_excludes

docs = [yaml.safe_load(open(p, encoding="utf-8"))
        for p in glob.glob(os.path.join(ROOT, "rules", "web", "**", "*.yml"), recursive=True)]
filters = [yaml.safe_load(open(p, encoding="utf-8")) for p in glob.glob(os.path.join(ROOT, "filters", "*.yml"))]
bad = n = 0
for line in open(os.path.join(ROOT, "tests", "web_cases.tsv"), encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    method, status, url, expected = line.rstrip("\n").split("\t")
    ev = {"cs-uri-query": url, "sc-status": status, "cs-method": method}
    got = sorted(d["name"] for d in docs if "detection" in d and rule_matches(d, ev)
                 and not any(d["name"] in f["filter"]["rules"] and filter_excludes(f, ev) for f in filters))
    want = [] if expected == "-" else expected.split(",")
    n += 1
    if got != want:
        bad += 1
        print(f"FAIL {method} {status} {url}\n     want {want}\n     got  {got}")
print(f"{n} cases, {bad} failed")
sys.exit(1 if bad else 0)
