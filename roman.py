"""roman converter module."""


def convert(input_str: str) -> int:
    """get roman string and return an integer"""
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50}
    int_value = 0
    for rom_ind, rom_val in enumerate(input_str):
        if rom_ind > 0 and \
                roman_values[rom_val] > roman_values[input_str[rom_ind - 1]]:
            int_value += roman_values[rom_val] - \
                                     2 * roman_values[input_str[rom_ind - 1]]
        else:
            int_value += roman_values[rom_val]
    return int_value
