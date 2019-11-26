"""Create a function for conversion roman number to integer"""


def convert(num: str) -> int:
    """Function for conversion roman number to integer"""
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    net = 0
    return sum([(net+rom[v]) if (k+1) == len(num) or rom[v] >= rom[num[k+1]]
                else (net-rom[v]) for k, v in enumerate(num)])
