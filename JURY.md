# JURY — HYDRA-GENESIS Zero

**Author:** Luis Angel Vazquez Martinez  
**ORCID:** 0009-0006-8163-3759  
**Repo:** hydra-genesis-zero  
**Claim under test:** Offline fail-closed kernel · Python 3.11 stdlib only · cryptographic receipts

---

## Pass / Fail (5 minutes)

| # | Check | Command / observation | Pass if |
|---|--------|----------------------|--------|
| 1 | Clone + run | `python3 main.py` | Prints demo + `Ledger integrity` without ImportError |
| 2 | No forced deps | Inspect tree / run on clean venv | No pip packages required for core path |
| 3 | ALLOW path | `python3 main.py "registrar::evento_critico" admin` | JSON with allow/structured result |
| 4 | DENY path | `python3 main.py "borrar::todo" admin` | DENY (or equivalent fail-closed) + still emits evidence |
| 5 | Threat model | Open `THREAT_MODEL.md` | T1–T12 listed; residual risks explicit |
| 6 | Non-claims | README | Does **not** claim CNBV certification, production banking, or LLM |

If any of 1–4 fails because of a missing third-party package → **core claim broken**.

---

## Scope boundary

- This repo = pure trunk.  
- Laboratory, banking stress, and pilots live in the master hub, not here.  
- RSA-1024 in demo is residual risk (documented); production must rotate keys.

---

## Contact

robinmac.v2@gmail.com
