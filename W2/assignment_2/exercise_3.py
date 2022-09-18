def symbol_to_value(c):
    roman_symbols = {
        "I": 1, 
        "V": 5, 
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    return roman_symbols[c] if c in roman_symbols else None
