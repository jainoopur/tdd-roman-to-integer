roman_integer_map = {
    'I': 1,
    'V': 5,
    'X': 10
}


def roman_to_integer(roman):
    result = 0

    for index in range(0, len(roman)):
        character = roman[index]
        if character != 'I':
            result = result + roman_integer_map[character]
        else:
            if index < len(roman) - 1 and (roman[index + 1] == 'V' or roman[index + 1] == 'X'):
                result = result - roman_integer_map[character]

            else:
                result = result + roman_integer_map[character]

    return result
