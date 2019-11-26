'''
Module
'''
DIGITS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def convert(strng: str) -> int:
    '''

    :param strng:
    :return:
    '''
    result, len_list = 0, len(strng)
    for i, _ in enumerate(strng):
        if i + 1 < len_list and DIGITS[strng[i]] < DIGITS[strng[i + 1]]:
            result -= DIGITS[strng[i]]
        else:
            result += DIGITS[strng[i]]
    return result
