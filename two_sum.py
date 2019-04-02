def two_sum(nums, target):
    index = {}
    for i in range(len(nums)):
        in_index = target - nums[i] in index
        if not in_index:
            index[nums[i]] = i
        if in_index:
            first = index[target - nums[i]]
            two = i
            return [first, two]

    return []


print(two_sum([2, 7, 11, 15], 9))
