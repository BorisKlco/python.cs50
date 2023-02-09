from vanity import plates

def test_plates():
    assert plates('CS50') == 'Valid'
    assert plates('CS05') == 'Invalid'
    assert plates('CS50P') == 'Invalid'
    assert plates('PI3.14') == 'Invalid'
    assert plates('H') == 'Invalid'
    assert plates('OUTATIME') == 'Invalid'
    assert plates('AAA222') == 'Valid'