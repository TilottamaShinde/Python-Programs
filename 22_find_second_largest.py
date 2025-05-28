# this program finds second largest number from a list. this program is example of list in python

def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    first = second = float('-inf')

    for num in numbers:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num

    return second if second != float('-inf') else None

#Example
nums = [10, 22, 34, 21, 40, 33]
result = find_second_largest(nums)
print("Second largest number : ", result)
