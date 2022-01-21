from ..util import *


def test_normalize_to_hex():
    assert "0x1.1p5" == normalize_to_hex("34."), "Should be 0x1.1p5"
    assert "0x1.8a3d70a3d70a4p0" == normalize_to_hex(
        "1.54"
    ), "Should be 0x1.8a3d70a3d70a4p0"
    assert "0xfe" == normalize_to_hex("254"), "Should be 0xfe"
    assert "0x1.fcp7" == normalize_to_hex("254."), "Should be 0x1.fcp7"
    assert "0x1.47ae147ae147bp-7" == normalize_to_hex(
        "1e-2"
    ), "Should be 0x1.47ae147ae147bp-7"

    assert "0x1.f4p9" == normalize_to_hex("1000."), "Should be 0x1.f4p9"
    assert "0x3e8" == normalize_to_hex("1000"), "Should be 0x3e8"
    assert "0x3e8" == normalize_to_hex("1e3"), "Should be 0x3e8"

    assert "0x1.4cccccccccccdp0" == normalize_to_hex(
        "1.3e0"
    ), "Should be 0x1.4cccccccccccdp0"
    assert "0x1.4cccccccccccdp0" == normalize_to_hex(
        "1.3"
    ), "Should be 0x1.4cccccccccccdp0"

    assert "0x0" == normalize_to_hex("0."), "Should be 0"
    assert "0x0" == normalize_to_hex("0"), "Should be 0"
    assert "0x0" == normalize_to_hex(".0"), "Should be 0"
    # 0e0 results in 0x0.p0
    assert "0x0.p0" == normalize_to_hex("0e0"), "Should be 0"
    assert "0x0" == normalize_to_hex("0e4"), "Should be 0"


def test_from_hex():
    assert "6736" == from_hex("0x34a.p3"), "Should be 6736"
    assert "6737.5" == from_hex("0x34a.3p3"), "Should be 6737.5"
    assert "255" == from_hex("0xff"), "Should be 255"

    assert "171" == from_hex("0xab."), "Should be 171"
    assert "171" == from_hex("ab."), "Should be 171"
    assert "171" == from_hex("0xab.0p0"), "Should be 171"
    assert "171" == from_hex("0xab.0"), "Should be 171"
    assert "171" == from_hex("ab.0"), "Should be 171"
    assert "171" == from_hex("0xa.bp4"), "Should be 171"
    assert "171" == from_hex("0xab"), "Should be 171"
