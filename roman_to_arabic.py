ARABIC_VALUE = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500
}


def roman_to_arabic(roman):
    count = 0
    pos = 0
    for char in roman:
        value = ARABIC_VALUE[char]
        if pos + 1 < len(roman) and value < ARABIC_VALUE[roman[pos + 1]]:
            count = count - value
        else:
            count = count + value
        pos = pos + 1
    return count
