def symbol_to_value(c):
    """Return decimal value of Roman symbol
    
    :param c: char representing a Roman symbol
    :type c: str

    :rtype: int
    :return: decimal value of Roman symbol
    
    .. note::
         If invaild symbol is passed, the function returns 0
    """
    roman_symbols = {
        "I": 1, 
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    
    return roman_symbols[c] if c in roman_symbols else 0

def roman_to_value(roman, ignore_sub_rule = False):
    """Return Roman number to decimal number
    
    :param roman: sequence of roman symbols, representing a Roman number
    :type roman: string
    :param ignore_sub_rule: defines if subtraction rule applies, defaults to False
    :type ignore_sub_rule: bool
    
    :return: decimal value of a Roman number
    :rtype: int
    """
    roman_decimal_value = 0

    if ignore_sub_rule:
        return sum([symbol_to_value(sym) for sym in roman])
    else:
        i = 0
        while i < len(roman):
            sym = {
                "left": symbol_to_value(roman[i]),
                "right": symbol_to_value(roman[i + 1])
                if i + 1 in range(len(roman))
                else -1,
            }

            # apply substraction rule if applicable
            if sym["right"] > sym["left"]:
                roman_decimal_value += sym["right"] - sym["left"]
                i += 1
            else:
                roman_decimal_value += sym["left"]
            i += 1

    return roman_decimal_value
