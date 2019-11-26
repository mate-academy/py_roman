"""Convert roman digits to arabian module"""


def convert(strng: str) -> int:
    """
    :param strng: string with roman digits
    :return: arabian result
    """
    roman = {"I": 1, "V": 5, "X": 10, "L": 50}
    result = 0
    for index, value in enumerate(strng):
        try:
            if roman[value] >= roman[strng[index+1]]:
                result += roman[value]
            elif roman[value] < roman[strng[index+1]]:
                result -= roman[value]
        except IndexError:
            result += roman[value]
    return result
