def int_to_roman(num):
    roman_symbol = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    roman_str = ''
    for key in roman_symbol:
        while num >= roman_symbol[key]:
            roman_str += key
            num -= roman_symbol[key]
    return roman_str


print(int_to_roman(20))
