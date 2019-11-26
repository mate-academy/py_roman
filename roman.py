"""
Roman number to integer
"""

def convert(str: str) -> int:
    """Conversion"""
    rome_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    rome_list = [rome_dict[i] for i in str]
    sum_nums = 0

    while rome_list:
        if rome_list.index(max(rome_list)) == 0:
            sum_nums += rome_list.pop(0)
        else:
            sum_nums -= rome_list.pop(0)
            sum_nums += rome_list.pop(0)

    return sum_nums
