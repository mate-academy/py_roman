"""The function for conversion roman number to integer"""


ROMAN_NUM = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }


def convert(roman_int: str) -> int:
    """General func"""
    result = 0
    for index, value in enumerate(roman_int):
        if index > 0 and ROMAN_NUM[value] > ROMAN_NUM[roman_int[index - 1]]:
            result += ROMAN_NUM[value] - 2 * ROMAN_NUM[roman_int[index - 1]]
        else:
            result += ROMAN_NUM[value]
    return result
