# find common elements

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

#Test
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

common = find_common_elements(a, b)
print("Common Elements : ", common)
