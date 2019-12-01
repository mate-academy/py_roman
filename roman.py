"""module"""


def convert(string_number: str) -> int:
    """convert number"""
    matches = {"I": 1, "V": 5, "X": 10, "L": 50}
    list_number = []
    for i in string_number:
        try:
            if matches[i] >= matches[string_number[string_number.index(i) + 1]]:
                list_number.append(matches[i])
            if matches[i] < matches[string_number[string_number.index(i) + 1]]:
                list_number.append(-matches[i])
        except IndexError:
            list_number.append(matches[i])
    return sum(list_number)
