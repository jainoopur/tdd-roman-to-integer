def roman_to_arabic(roman):
    count = 0
    pos = 0
    for char in roman:
        if char == 'I':
            if pos + 1 < len(roman) and roman[pos + 1] != 'I':
                count = count - 1
            else:
                count = count + 1
        elif char == 'V':
            count = count + 5
        elif char == 'X':
            count = count + 10
        pos = pos + 1
    return count

