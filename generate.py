##Create a number guessing game,where you have to generate a random number in between 1 to 100 and user have to prompt a number for guess.
# if its high or low number let the user know and guide them through the process to guess correct number.

import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

print("Welcome to the Number Guessing Game!")
guess_number()
