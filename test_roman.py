import roman


def test_1():
    assert roman.convert("I") == 1


def test_2():
    assert roman.convert("II") == 2


def test_3():
    assert roman.convert("III") == 3


def test_4():
    assert roman.convert("IV") == 4


def test_5():
    assert roman.convert("V") == 5


def test_16():
    assert roman.convert("XVI") == 16


def test_14():
    assert roman.convert("XIV") == 14


def test_25():
    assert roman.convert("XXV") == 25


def test_43():
    assert roman.convert("XLIII") == 43

