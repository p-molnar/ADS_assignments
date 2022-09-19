def symbol_to_value(c):
    """Return decimal value of Roman symbol
    
    :param c: a char representing a roman symbol
    :type c: str

    :rtype: int
    :return: decimal value of Roman symbol if vaild symbol, else None
    """
    roman_symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    return roman_symbols[c] if c in roman_symbols else 0


def roman_to_value(roman, ignore_sub_rule=False):
    """Convert and return Roman number to decimal
    
    :param roman: sequence of roman symbols, representing a Roman number
    :type roman: string
    :param ignore_sub_rule: defines if subtraction rule applies
    :type ignore_sub_rule: bool
    
    :return: decimal value of a Roman number
    :rtype: int
    """
    roman_decimal_value = 0

    if ignore_sub_rule == True:
        for symbol in roman:
            roman_decimal_value += symbol_to_value(symbol)
    else:
        idx = 0
        while idx < len(roman):
            val_1 = symbol_to_value(roman[idx])
            val_2 = (
                symbol_to_value(roman[idx + 1]) if idx + 1 in range(len(roman)) else -1
            )
            if val_1 < val_2:
                roman_decimal_value += val_2 - val_1
                idx += 1
            else:
                roman_decimal_value += val_1
            idx += 1

    return roman_decimal_value
