from ..util import *

def test_normalize_to_hex():
    assert '0x1.1p5' == normalize_to_hex(34.), "Should be 0x1.1p5"
    assert '0x1.8a3d70a3d70a4p0' == normalize_to_hex(1.54), "Should be 0x1.8a3d70a3d70a4p0"

def test_from_hex():
    assert '6736' == from_hex('0x34a.p3'), "Should be 6736"
    assert '6737.5' == from_hex('0x34a.3p3'), "Should be 6737.5"