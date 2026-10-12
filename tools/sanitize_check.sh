#!/bin/bash
# sanitize_check.sh <dir>: fail if the tree contains private addresses or internal names.
# Patterns for internal names come from SANITIZE_EXTRA (one regex per line, kept outside this repo).
set -u
D="${1:-.}"
PAT='(^|[^0-9.])(10\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|172\.(1[6-9]|2[0-9]|3[01])\.[0-9]{1,3}\.[0-9]{1,3}|192\.168\.[0-9]{1,3}\.[0-9]{1,3})([^0-9]|$)'
rc=0
if grep -rInE --exclude-dir=.git "$PAT" "$D"; then echo "FAIL: private IPv4 address" >&2; rc=1; fi
if [ -n "${SANITIZE_EXTRA:-}" ] && [ -f "$SANITIZE_EXTRA" ]; then
  if grep -rIniE --exclude-dir=.git -f "$SANITIZE_EXTRA" "$D"; then echo "FAIL: internal name" >&2; rc=1; fi
fi
[ $rc -eq 0 ] && echo "sanitize: clean"
exit $rc
