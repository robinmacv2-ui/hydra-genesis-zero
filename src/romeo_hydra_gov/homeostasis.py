"""Minimal homeostasis marker for Genesis Zero."""

def check_homeostasis(state: dict) -> bool:
    """Return True if basic invariants hold (fail-closed helper)."""
    if not isinstance(state, dict):
        return False
    return "status" in state
