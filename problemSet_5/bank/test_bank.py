from bank import helloBank

def test_bank():
    assert helloBank('hello') == '$0'
    assert helloBank('hi') == '$20'
    assert helloBank('sup') == '$100'