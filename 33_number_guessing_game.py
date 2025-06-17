import random

number = random.randint(1, 100)
attempts = 0

print("Guess the number between 1 and 100 ")

while True:
    try:
        guess = int(input("Guess your number : "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You guessed in {attempts} tries")
            break
    except ValueError:
        print("Please enter a valid number.")
