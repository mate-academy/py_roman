"""doc-sting"""
from typing import List


def convert(roman: str) -> int:
    """
    Converts roman number to integer
    :param roman: str
    :return: int
    """
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    lst_rom = list(roman)
    integers = []            # type: List[int]
    while lst_rom:
        if not integers or integers[-1] >= rom_int[lst_rom[0]]:
            integers.append(rom_int[lst_rom.pop(0)])
        else:
            integers[-1] = rom_int[lst_rom.pop(0)] - integers[-1]

    return sum(integers)
