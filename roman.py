"""module docstring"""
def convert(roman_numeral):
    """function docstring"""
    basic_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    decimal_num = 0
    for seq, _value in enumerate(roman_numeral):
        if seq > 0 and basic_symbols[roman_numeral[seq]] > \
                basic_symbols[roman_numeral[seq - 1]]:
            decimal_num += basic_symbols[roman_numeral[seq]] - \
                           2 * basic_symbols[roman_numeral[seq - 1]]
        else:
            decimal_num += basic_symbols[roman_numeral[seq]]
    return decimal_num
