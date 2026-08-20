from __future__ import annotations
from typing import Any, Dict
from .rdd_receipt import seal_receipt, write_receipt
from .paths import receipts_final

def execute_allowed(candidate: Dict[str, Any]) -> Dict[str, Any]:
    """Execute only after gate has allowed. Always seals post-receipt."""
    result = {
        "status": "executed",
        "candidate_id": candidate.get("id"),
        "tool": candidate.get("tool"),
    }
    receipt = seal_receipt({"candidate": candidate, "result": result}, rule="post_allow")
    write_receipt(receipt, receipts_final())
    return result
