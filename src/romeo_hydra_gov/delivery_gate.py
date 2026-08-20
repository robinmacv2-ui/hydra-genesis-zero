from __future__ import annotations
from typing import Any, Dict

def authorize_delivery(decision: Dict[str, Any]) -> bool:
    """Final delivery authorization — fail-closed."""
    if not decision:
        return False
    if decision.get("delivery_authorization") == "denied":
        return False
    return decision.get("status") == "executed" or "id" in decision
