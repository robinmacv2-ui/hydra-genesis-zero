#!/usr/bin/env python3
"""main.py — HYDRA-GENESIS Zero v0.2.1 entrypoint"""
from faro import run_gate, Ledger, ROOT
import json, sys

def demo():
    print("=== HYDRA-GENESIS Zero v0.2.1 · RSA + Formal DFA ===")
    print(f"ROOT: {ROOT}\n")
    cases = [
        ("ver::cliente_001", "operador"),
        ("mover::archivo_x", "operador"),
        ("registrar::evento_critico", "admin"),
        ("bloquear::usuario_malicioso", "admin"),
        ("borrar::todo", "admin"),
    ]
    for raw, role in cases:
        print(f"→ {raw!r} role={role}")
        try:
            result = run_gate(raw, role)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            from faro import Receipt
            ok = Ledger().verify_receipt(Receipt(**result))
            print(f"  signature_valid: {ok}")
        except Exception as e:
            print(f"  EXCEPTION: {e}")
        print("-" * 50)
    led = Ledger()
    print(f"Ledger integrity (hash+RSA): {led.verify_integrity()}")
    print(f"Chain length: {len(led._chain)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(run_gate(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "operador"), indent=2))
    else:
        demo()
