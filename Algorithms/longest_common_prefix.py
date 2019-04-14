def longest_common_prefix(strs):
    """
    :param strs: List
    :return: String
    """
    if not strs:
        return ''
    min_str = min(strs,  key=len)

    for index, letter in enumerate(min_str):
        for last in strs:
            if last[index] != letter:
                return min_str[:index]
    return min_str

    # return min_str


print(longest_common_prefix(["dog","racecar","car"]))
