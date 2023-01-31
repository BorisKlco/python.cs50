from twttr import twttr

def test_twttr():
    assert twttr('twitter') == 'twttr'
    assert twttr('Twitter') == 'Twttr'
    assert twttr('TWITTER') == 'TWTTR'