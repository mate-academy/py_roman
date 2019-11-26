"""
module convert
"""


def convert(roman_num: str) -> int:
    """
    Conversion roman number to integer.
    :param roman_num: str
    :return: int
    """
    result = 0
    roman_num = roman_num.upper()
    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i, _ in enumerate(roman_num):
        if i + 1 < len(roman_num) and rome_dict[roman_num[i]] < rome_dict[roman_num[i + 1]]:
            result -= rome_dict[roman_num[i]]
        else:
            result += rome_dict[roman_num[i]]

    return result
