# Find the missing number in a list from 1 to N

def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example usage
nums = [1, 2, 3, 5]     # Missing number is 4
n = 5                   # Since its from 1 to 5

missing = find_missing_number(nums, n)
print("Missing number is : ", missing)
