from twttr import shorten

def test_shorten_b():
    assert shorten("twitter") == "twttr"
    assert shorten("good") == "gd"
    assert shorten("hello") == "hll"

def test_shorten_m():
    assert shorten("TwiTtEr") == "TwTtr"
    assert shorten("good") == "gd"
    assert shorten("HELLO") == "HLL"

def test_shorten_o():
    assert shorten("aeouiAEOUI") == ""
    assert shorten("") == ""
    assert shorten("good,1") == "gd,1"


