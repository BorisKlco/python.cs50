from fuel import fuel

def test_fuel():
    assert fuel('3/4') == '75%'
    assert fuel('1/4') == '25%'
    assert fuel('4/4') == 'F'
    assert fuel('0/4') == 'E'
    assert fuel('4/0') == 'error'
    assert fuel('three/four') == 'error'
    assert fuel('5/4') == 'error'