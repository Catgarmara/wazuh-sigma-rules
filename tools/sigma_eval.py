"""sigma_eval.py: minimal offline evaluator for the Sigma subset this repo uses.

Supports: field|re, field|re|i, field|contains, field|startswith, plain equality, value lists (OR),
multiple fields in a selection (AND), conditions built from identifiers, 'and', 'or', 'not',
parentheses, '1 of <prefix>*', 'all of <prefix>*'. Regexes run with the `regex` module (PCRE-like).
An event is a dict keyed by Sigma taxonomy field names (cs-uri-query, sc-status, cs-method, ...).
"""
import re
import regex


def _match_value(mods, pattern, value):
    if value is None:
        return False
    v = str(value)
    if "re" in mods:
        flags = regex.IGNORECASE if "i" in mods else 0
        return regex.search(str(pattern), v, flags) is not None
    if "contains" in mods:
        return str(pattern).lower() in v.lower()
    if "startswith" in mods:
        return v.lower().startswith(str(pattern).lower())
    if "endswith" in mods:
        return v.lower().endswith(str(pattern).lower())
    return v.lower() == str(pattern).lower()


def match_selection(sel, event):
    if isinstance(sel, list):  # list of maps = OR
        return any(match_selection(s, event) for s in sel)
    for key, want in sel.items():
        field, *mods = key.split("|")
        vals = want if isinstance(want, list) else [want]
        if "all" in mods:
            if not all(_match_value(mods, p, event.get(field)) for p in vals):
                return False
        elif not any(_match_value(mods, p, event.get(field)) for p in vals):
            return False
    return True


_TOK = re.compile(r"\s*(\(|\)|\band\b|\bor\b|\bnot\b|1 of [\w*]+|all of [\w*]+|[\w*]+)\s*")


def eval_condition(cond, detections, event):
    toks = [t for t in _TOK.findall(cond) if t]
    pos = 0

    def ident(name):
        if name.startswith(("1 of ", "all of ")):
            q, pat = name.split(" of ")
            pat = pat.replace("them", "*")
            keys = [k for k in detections if re.fullmatch(pat.replace("*", ".*"), k)]
            res = [match_selection(detections[k], event) for k in keys]
            return any(res) if q == "1" else all(res)
        return match_selection(detections[name], event)

    def expr():
        nonlocal pos
        v = term()
        while pos < len(toks) and toks[pos] == "or":
            pos += 1
            r = term()
            v = v or r
        return v

    def term():
        nonlocal pos
        v = factor()
        while pos < len(toks) and toks[pos] == "and":
            pos += 1
            r = factor()
            v = v and r
        return v

    def factor():
        nonlocal pos
        t = toks[pos]
        if t == "not":
            pos += 1
            return not factor()
        if t == "(":
            pos += 1
            v = expr()
            pos += 1  # ')'
            return v
        pos += 1
        return ident(t)

    return expr()


def rule_matches(doc, event):
    det = {k: v for k, v in doc["detection"].items() if k != "condition"}
    return eval_condition(doc["detection"]["condition"], det, event)


def filter_excludes(fdoc, event):
    """True when the filter removes this event (the filter's condition evaluates False)."""
    f = fdoc["filter"]
    det = {k: v for k, v in f.items() if k not in ("rules", "condition")}
    return not eval_condition(f["condition"], det, event)
