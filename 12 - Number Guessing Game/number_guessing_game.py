import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\n\n")

print("I'm thinking of a number between 1 and 100.\n")
difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")

attempts = 10 if difficulty == "easy" else 5
target_number = random.randint(1, 100)


def evaluate_guess(current_guess):
    if current_guess == target_number:
        print(f"\nYou got it! The answer was {target_number}.")
        return "win"
    elif current_guess > target_number:
        print("\nToo high.")
    elif current_guess < target_number:
        print("\nToo low")


for i in range(attempts):
    player_guess = int(input("Make a guess: "))
    if evaluate_guess(player_guess) == "win":
        break
    if i < attempts - 1:
        print(f"You have {attempts - 1 - i} remaining to guess the number.")
    if i == attempts - 1:
        print("You have run out of guesses.  Game over!\n")

input("Press Enter to exit...")
