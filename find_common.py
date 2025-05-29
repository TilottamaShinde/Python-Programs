# find common elements from list using set

def find_common(list1, list2):
    return list(set(list1) & set(list2))

#Test
a = [1, 2, 5, 6]
b = [5, 1, 4, 6]

print("Common Elements : ", find_common(a,b))