# THREAT MODEL — HYDRA-GENESIS Zero / ROMEO-HYDRA v0.2.1

**Alcance:** Núcleo offline fail-closed + firma digital asimétrica RSA-SHA256 (pure Python stdlib).

## Controles

| ID | Amenaza | Control | Estado |
|----|---------|---------|--------|
| T1 | Path traversal | Path.resolve + relative_to(ROOT) | Mitigado |
| T2 | Verbo fuera de conjunto | VERB_CLOSED_SET + parse fail-closed | Mitigado |
| T3 | Prompt/command injection | Regex formal + rechazo total | Mitigado |
| T4 | Rotura de cadena | verify_integrity recalcula SHA-256 | Mitigado |
| T5 | Escalada de privilegios | ROLE_CAPS | Mitigado |
| T6 | Parse permisivo | AST frozen + re.fullmatch | Mitigado |
| T7 | Dependencias terceros | stdlib only | Mitigado |
| T8 | Estado DFA inválido | TRANSITIONS → ERROR → DENY | Mitigado |
| T9 | Ledger vacío | prev_hash = 64 ceros | Mitigado |
| T10 | Falsificación de recibo | Firma RSA del payload canónico | **Mitigado v0.2.1** |
| T11 | Clave privada filtrada | private.json mode 0600 | Mitigado |
| T12 | Sustitución de clave pública | n embebido en cada recibo | Mitigado |

## Residual
- RSA-1024 demo (regenerar 2048+ para producción).
- Sin CA externa (diseño offline).
- Single-writer ledger.

**Principio:** Fail-closed real. Cualquier fallo de parse, capability, DFA, path, hash o firma RSA → DENY + receipt firmado.
