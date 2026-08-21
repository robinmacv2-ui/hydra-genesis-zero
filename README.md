# HYDRA-GENESIS Zero (HGZ-0)

**Immutable pure offline fail-closed kernel.**  
Python 3.11 · **stdlib only** · Zero third-party deps · Zero banking · Zero cloud.

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Stdlib only](https://img.shields.io/badge/deps-stdlib%20only-success.svg)](#)
[![Offline](https://img.shields.io/badge/offline-100%25-green.svg)](#)
[![Fail-closed](https://img.shields.io/badge/gate-FAIL--CLOSED-black.svg)](#)

> Extracted 2026-08-20. This is the pure trunk — not the laboratory.

---

## Jury path (≤ 60 seconds)

```bash
git clone --depth 1 https://github.com/robinmacv2-ui/hydra-genesis-zero.git
cd hydra-genesis-zero
python3 main.py
```

No `pip install`. No network after clone. Expected: demo of gate decisions + ledger integrity line.

### Single-command probes

```bash
# ALLOW path (role with capability)
python3 main.py "registrar::evento_critico" admin

# DENY path (verb outside closed set / capability)
python3 main.py "borrar::todo" admin
```

Pass criteria: every decision returns structured JSON; DENY still produces a receipt; ledger integrity reports true after demo.

---

## What this is

| Piece | Role |
|-------|------|
| `main.py` | Reproducible entrypoint |
| `faro.py` | Gate + RSA-SHA256 ledger (stdlib) |
| `romeo_agent/` | Admissible / lineage / runtime skeleton |
| `src/` | Formal DFA surface |
| `tests/` | Unit surface |
| `THREAT_MODEL.md` | Threat controls T1–T12 |
| `JURY.md` | Pass/fail checklist for committees |

---

## What this is NOT

- Not a production banking system  
- Not CNBV-certified  
- Not an LLM  
- Not dependent on numpy, cloud APIs, or shell escape  

---

## Ecosystem map

| Repo | Role |
|------|------|
| **hydra-genesis-zero** (this) | Immutable pure kernel (MRU) |
| [romeo-hydra-master-repository-hub](https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub) | Pilot + DOI + product surface |
| [romeo-hydra-quantik](https://github.com/robinmacv2-ui/romeo-hydra-quantik) | Public evaluation door |

---

## License

Dual: AGPL-3.0 (evaluation / non-commercial) · Commercial EMMOROR (regulated production).

**Author:** Luis Angel Vazquez Martinez  
**ORCID:** [0009-0006-8163-3759](https://orcid.org/0009-0006-8163-3759)  
**Contact:** robinmac.v2@gmail.com
