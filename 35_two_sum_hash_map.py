def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


#Exmaple usage
print(two_sum([1,6,7,3], 9))
