def remove_duplicates(nums):
    """
    循环判断列表里面的前后两个数, 如果前后相等就删除一个 然后增加1 继续判断 直到大于数组长度就结束
    :param nums: List[int]
    :return: Int
    """
    _next = 1
    while _next < len(nums):
        if nums[_next] == nums[_next-1]:
            del nums[_next]
        else:
            _next += 1

    return len(nums)


print(remove_duplicates([1, 1, 2]))
