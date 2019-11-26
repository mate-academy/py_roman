"""
docstring
"""
import roman


def test_1():
    """

    :return:
    """
    assert roman.convert("I") == 1


def test_2():
    """

    :return:
    """
    assert roman.convert("II") == 2


def test_3():
    """

    :return:
    """
    assert roman.convert("III") == 3


def test_4():
    """

    :return:
    """
    assert roman.convert("IV") == 4


def test_5():
    """

    :return:
    """
    assert roman.convert("V") == 5


def test_16():
    """

    :return:
    """
    assert roman.convert("XVI") == 16


def test_14():
    """

    :return:
    """
    assert roman.convert("XIV") == 14


def test_25():
    """

    :return:
    """
    assert roman.convert("XXV") == 25


def test_43():
    """

    :return:
    """
    assert roman.convert("XLIII") == 43


