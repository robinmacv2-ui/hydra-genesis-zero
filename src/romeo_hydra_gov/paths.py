from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECEIPTS = ROOT / "receipts"
RECEIPTS_CANDIDATES = RECEIPTS / "candidates"
RECEIPTS_FINAL = RECEIPTS / "final"

def receipts_candidates() -> Path:
    RECEIPTS_CANDIDATES.mkdir(parents=True, exist_ok=True)
    return RECEIPTS_CANDIDATES

def receipts_final() -> Path:
    RECEIPTS_FINAL.mkdir(parents=True, exist_ok=True)
    return RECEIPTS_FINAL
