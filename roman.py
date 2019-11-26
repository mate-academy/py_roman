"""
docstring
"""


def convert(string: str) -> int:
    """

    :param string:
    :return:
    """
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
    res = 0
    for index, item in enumerate(string):
        try:
            if romans[item] < romans[string[index+1]]:
                res -= romans[item]
            else:
                res += romans[item]
        except IndexError:
            res += romans[item]
    return res
