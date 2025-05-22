# move zeros to end

def move_zero_to_end(arr):
    non_zero_index = 0

    #move all non zero elements to front
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i]= arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr

# test cases
arr1 = [1,2,0,3,12]
arr2 = [1,2,0,0,4,0,5]

print("Before : ", arr1)
print("After : ", move_zero_to_end(arr1))

print("Before : ", arr2)
print("After : ", move_zero_to_end(arr2))
