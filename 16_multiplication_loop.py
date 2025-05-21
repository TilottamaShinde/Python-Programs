n = 5
print("Multiplication table for ",n," is : ")

#iterate over numbers in the range 1 to n
for row in range(1,n+1):
    for col in range(1,n+1):
        print(row*col, end = "\t")
    print()

