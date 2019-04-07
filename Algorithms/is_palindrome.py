def is_palindrome(x):
    if x < 0:
        return False
    str_x = str(x)[::-1]
    return x == int(str_x)


print(is_palindrome(10))
