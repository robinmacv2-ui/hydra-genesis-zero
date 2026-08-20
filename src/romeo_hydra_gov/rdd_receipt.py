from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

def _sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

def seal_receipt(payload: Dict[str, Any], rule: str = "default") -> Dict[str, Any]:
    """Seal a decision into an immutable receipt (WORM style)."""
    ts = datetime.now(timezone.utc).isoformat()
    body = {
        "timestamp_utc": ts,
        "rule": rule,
        "payload": payload,
    }
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"))
    body["sha256"] = _sha256(canonical)
    return body

def write_receipt(receipt: Dict[str, Any], folder: Path) -> Path:
    folder.mkdir(parents=True, exist_ok=True)
    rid = receipt.get("sha256", "unknown")[:16]
    path = folder / f"receipt_{rid}.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    return path
