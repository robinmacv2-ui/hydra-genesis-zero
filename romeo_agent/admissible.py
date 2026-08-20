"""Gate ex-ante: conjunto admisible C. Fail-closed. O(1).

Any verb not in VERBOS_ADMISIBLES => deny.
"""
from __future__ import annotations

VERBOS_ADMISIBLES = {
    "echo",
    "status",
    "help",
    "pwd",
    "ls",
    "cat",
    "hash",
    "hashfile",
    "log",
    "verify",
    "score",
    "audit",
    "lineage",
}

N_MIN, N_MAX = 1, 1000
CAT_MAX_BYTES = 64 * 1024

def _path_safe(path: str) -> bool:
    if not path or not isinstance(path, str):
        return False
    p = path.strip()
    if not p or ".." in p:
        return False
    if p.startswith("/") or p.startswith("~"):
        return False
    return True

def is_admissible(verb: str, args: dict | None = None) -> bool:
    """Fail-closed: only closed set of verbs is allowed."""
    if not verb or not isinstance(verb, str):
        return False
    v = verb.strip().lower()
    if v not in VERBOS_ADMISIBLES:
        return False
    args = args or {}
    if v in ("cat", "hashfile", "ls") and "path" in args:
        return _path_safe(str(args["path"]))
    return True
