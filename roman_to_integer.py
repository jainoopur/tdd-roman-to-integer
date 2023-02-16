
def is_char_I(char):
    return char == 'I'


def get_value(char):
    if char == 'I':
        return 1
    if char == 'V':
        return 5
    if char == 'X':
        return 10
    if char == 'L':
        return 50


def roman_to_integer(roman):
    # II
    sum = 0
    prev_char = None
    for char in roman:
        sum = sum + get_value(char)
        if is_char_I(prev_char) and not is_char_I(char):
            sum = sum - 2 * get_value(prev_char)
        prev_char = char

    return sum
