ROMAN_TO_INTEGER = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def roman_to_integer(roman):
    ans = 0
    for index in range(len(roman)):
        curr_char = roman[index]
        if curr_char not in ROMAN_TO_INTEGER.keys():
            raise ValueError('Invalid roman numeral')
        current_char_value = ROMAN_TO_INTEGER[curr_char]
        if index < len(roman) - 1:
            next_char = roman[index + 1]
            next_char_value = ROMAN_TO_INTEGER[next_char]
            if next_char_value > current_char_value:
                ans = ans - current_char_value
            else:
                ans = ans + current_char_value
        else:
            ans = ans + current_char_value
    return ans
