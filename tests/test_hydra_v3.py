#!/usr/bin/env python3
"""tests/test_hydra_v3.py — Hard tests + RSA"""
import sys
from pathlib import Path
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from faro import (parse, VERB_CLOSED_SET, ROLE_CAPS, TRANSITIONS, STATES,
                  Ledger, run_gate, confined, ROOT, generate_rsa_keypair,
                  rsa_sign, rsa_verify, Receipt, _compute_hash)

def test_prompt_injection():
    for inj in ["ver::entidad; DROP", "ver::entidad`rm`", "IGNORE::SYSTEM", "ver::x\x00"]:
        with pytest.raises(ValueError):
            parse(inj)
        assert run_gate(inj, "admin")["decision"] == "DENY"

def test_path_traversal():
    for a in ["../../etc/passwd", "/etc/passwd", "foo/../../bar"]:
        with pytest.raises(PermissionError):
            confined(a)
    assert confined(ROOT / "delta_ledger_registry.json") == (ROOT / "delta_ledger_registry.json").resolve()

def test_verbo_fuera_conjunto():
    for v in ["borrar", "ejecutar", "sudo", "rm"]:
        with pytest.raises(ValueError):
            parse(f"{v}::entidad")
    for v in VERB_CLOSED_SET:
        if v != "denegar":
            assert parse(f"{v}::test").verbo == v

def test_prev_hash_integrity(tmp_path, monkeypatch):
    import faro
    original = faro.confined
    faro.confined = lambda p: Path(p)
    try:
        led = Ledger(str(tmp_path / "t.json"))
        led.append("ver", "e1", "operador", "ALLOW")
        led.append("mover", "e2", "operador", "ALLOW")
        assert led.verify_integrity() is True
        led._chain[1].signature = "deadbeef"
        assert led.verify_integrity() is False
    finally:
        faro.confined = original

def test_fuzzing_verbo():
    import random, string
    alphabet = string.ascii_lowercase + string.digits + "_"
    for _ in range(100):
        fuzz = "".join(random.choice(alphabet) for _ in range(random.randint(1, 8)))
        raw = f"{fuzz}::entidad"
        if fuzz in VERB_CLOSED_SET:
            assert parse(raw).verbo == fuzz
        else:
            with pytest.raises(ValueError):
                parse(raw)

def test_rsa_sign_verify():
    pub, priv = generate_rsa_keypair(512)
    msg = b"ROMEO-HYDRA-test"
    sig = rsa_sign(msg, priv)
    assert rsa_verify(msg, sig, pub) is True
    assert rsa_verify(b"tampered", sig, pub) is False

def test_receipt_signature_roundtrip():
    r = run_gate("ver::cliente_firma", "operador")
    assert r["signature"] and r["public_key_n"]
    assert Ledger().verify_receipt(Receipt(**r)) is True

def test_dfa_and_caps():
    assert "INIT" in STATES and TRANSITIONS[("INIT", "ver")] == "PARSED"
    assert "bloquear" not in ROLE_CAPS["operador"]
    assert "registrar" in ROLE_CAPS["admin"]

def test_gate_deny_allow():
    assert run_gate("bloquear::x", "operador")["decision"] == "DENY"
    r = run_gate("registrar::evento", "admin")
    assert r["decision"] == "ALLOW" and len(r["signature"]) > 10
