def reverse(x):
    _max = 2**31
    _min = -2**31
    str_x = str(x)
    if -10 < x < 10:
        return x
    if x < 0:
        temp_x = str_x.split('-')[1]
        int_x = int(temp_x[::-1])
        reverse_num = -int_x
    else:
        reverse_num = int(str_x[::-1])
    if reverse_num > _max or reverse_num < _min:
        return 0
    return reverse_num


print(reverse(-10))
