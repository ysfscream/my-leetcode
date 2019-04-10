def roman_to_int(s):
    """
    首先建立一个HashMap来映射符号和值
    然后对字符串从左到右来 如果当前字符代表的值不小于其右边 就加上该值 否则就减去该值
    以此类推到最左边的数

    :param s: string
    :return: int
    """
    int_symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    roman_num = 0
    for index in range(len(s)):
        left = int_symbol[s[index]]
        if index + 1 < len(s) and left < int_symbol[s[index + 1]]:
            roman_num -= left
        else:
            roman_num += left

    return roman_num


print(roman_to_int('III'))
