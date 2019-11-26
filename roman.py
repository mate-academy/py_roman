"""Convert roman digits to arabian module"""


def convert(strng: str) -> int:
    """
    :param strng: string with roman digits
    :return: arabian result
    """
    roman_digits = {"I": 1, "V": 5, "X": 10, "L": 50}
    result = 0
    index = 0
    strng = strng[::-1]
    while index < len(strng):
        try:
            try:
                if roman_digits[strng[index]] == roman_digits[strng[index+1]] \
                        == roman_digits[strng[index+2]]:
                    result += roman_digits[strng[index]]*3
                    index += 3
                    continue
            except IndexError:
                pass
            if roman_digits[strng[index]] > roman_digits[strng[index+1]]:
                result += roman_digits[strng[index]] - roman_digits[strng[index+1]]
            else:
                result += roman_digits[strng[index]] + roman_digits[strng[index+1]]
            index += 2
        except IndexError:
            result += roman_digits[strng[index]]
            index += 1
    return result
