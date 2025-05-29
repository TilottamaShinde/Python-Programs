# program to remove duplicates from list using set
def remove_duplicates(input_list):
    return list(set(input_list))

#Example usage
data = [1,2,3,3,4,5,5,1,5]
unique_data = remove_duplicates(data)
print("Unique elements are : ", unique_data)

# output
# Unique elements are :  [1, 2, 3, 4, 5]
