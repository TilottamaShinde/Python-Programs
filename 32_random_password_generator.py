import random
import string

def generate_password(length = 12):
    if length < 4:
        return "Password should be at least 4 characters long."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        user_length = int(input("Enter the desired password length: "))
        print("Generate Password: ", generate_password(user_length))
    except ValueError:
        print("Please enter a valid number.")
