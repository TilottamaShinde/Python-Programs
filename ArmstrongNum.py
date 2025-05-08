# This program finds armstrong number

num = int(input("Enter the number : "))
original_num = num
num_digit = len(str(num))

sum_of_power = 0

while num > 0:
    digit = num % 10
    sum_of_power += digit ** num_digit
    num = num // 10

if sum_of_power == original_num:
    print("It is Armstrong Number")
else:
    print("It is not Armstrong Number")