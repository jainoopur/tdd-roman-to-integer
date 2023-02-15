ARABIC_VALUE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50
}


def roman_to_arabic(roman):
    count = 0
    pos = 0
    for char in roman:
        value = ARABIC_VALUE[char]
        if pos + 1 < len(roman) and (char == 'I' or char == 'X'):
            next_char = roman[pos + 1]
            next_char_value = ARABIC_VALUE[next_char]
            if value < next_char_value:
                count = count - value
            else:
                count = count + value
        else:
            count = count + value
        pos = pos + 1
    return count
