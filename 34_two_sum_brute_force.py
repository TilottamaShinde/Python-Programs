
# Two sum problem using Basic Brute Force Method

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if  nums[i] + nums[j] == target:
                return [i,j]

# Example usage
print(two_sum([2,7,11, 15], 18))


'''
Output:
[1, 2]

'''
