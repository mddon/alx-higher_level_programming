#!/usr/bin/python3
def roman_to_int(roman_string):

    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    sum = 0

    for p in range(len(roman_string)):
        if roman_numerals.get(roman_string[p], 0) == 0:
            return 0

        if (p != (len(roman_string) - 1) and
                roman_numerals[roman_string[p]] < roman_numerals[roman_string[p + 1]]):
            sum += roman_numerals[roman_string[p]] * -1
        else:
            sum += roman_numerals[roman_string[p]]
    return sum
