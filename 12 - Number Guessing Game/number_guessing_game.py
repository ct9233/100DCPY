import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\n")

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")

attempts = 10 if difficulty == "easy" else 5
target_number = random.randint(1, 100)

def evaluate_guess(current_guess):
        if current_guess == target_number:
            print(f"You got it! The answer was {target_number}.")
        elif current_guess > target_number:
            print("Too high.")
        elif current_guess < target_number:
            print("Too low")

for i in range(attempts):
    player_guess = int(input("Make a guess: "))
    evaluate_guess(player_guess)
    if i < 5:
        print(f"You have {attempts - 1 - i} remaining to guess the number.")
    


print("You have run out of guesses.  Game over!")
