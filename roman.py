"""docstring"""


def convert(string: str) -> int:
    """convert roman to int"""
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50
    }
    output = 0
    for i, char in enumerate(string):
        try:
            if roman[char] >= roman[string[i + 1]]:
                output += roman[char]
            else:
                output -= roman[char]
        except IndexError:
            output += roman[char]
    return output
