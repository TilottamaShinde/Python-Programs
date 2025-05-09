# Program to find out factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# usage
print(factorial(3))
