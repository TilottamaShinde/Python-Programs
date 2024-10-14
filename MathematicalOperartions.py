# This program performs basic mathematical operations such as
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. DivisionImpossible
# 5. Percentage

#Function for addition
def add(num1,num2):
    return num1 + num2

#Function for Subtraction
def sub(num1,num2):
    return num1 - num2

#Function for Multiplication
def multiply(num1, num2):
    return num1 * num2

#Function for Division
def divide(num1,num2):
    if num2 == 0:
        return "Error:Division by 0 is undefined "
    return num1 / num2

# Function for calculation percentage
def percentage(total,part):
    if total == 0:
        return "Error: Total Cannot be 0 while calculating percentage"
    return (part / total) * 100


def display_menu():
    print("Select Operation : ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Percentage")

def get_user_input():
    try:
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))
        return num1,num2
    except ValueError:
        print("Invalid Value. Enter numeric values only")
        return None, None

def get_percentage_input():
    try:
        total = float(input("Enter the total : "))
        part = float(input("Enter the part : "))
        return total, part
    except ValueError:
        print("Invalid Value. Enter numeric values only")
        return None, None

def main():
    while True:
        display_menu()

        #Enter operation choice
        choice = input("Enter your choice 1/2/3/4/5 or 'q' to quite : ")
        if choice == 'q':
            print("Exiting the program.")
            break

        if choice in('1','2','3','4'):
            num1, num2 = get_user_input()

            if num1 is None or num2 is None:
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {sub(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

        elif choice == '5':
            total, part = get_percentage_input()
            if total is None or part is None:
                continue
            print(f"Result: {part} is {percentage(total,part)}% of {total} ")

        else:
            print("Invalid Choice. Please select a valid options")

if __name__ == "__main__":
    main()
