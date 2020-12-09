import os
import random

from hangman_words import word_list

chosen_word = random.choice(word_list)

lives = 6
game_end = False
display = []
guesses = []

for letter in chosen_word:
    display.append("_")

from hangman_art import logo, stages

print(logo)
print(stages[lives])
print(f"{' '.join(display)}\n")

while not game_end:
    guess = input("Guess a letter: ").lower()
    os.system("cls")

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            if guess in guesses:
                print("You have already guessed that letter.")
            else:
                guesses.append(guess)
    if guess not in display:
        if guess in guesses:
            print("You have already guessed that letter.")
        else:
            if lives > 1:
                print(f"Letter '{guess}' is not in word.  One step closer to death...")
                guesses.append(guess)
                lives -= 1
            else:
                game_end = True
                print(stages[lives - 1])
                print("You lose.")
                input("\nPress Enter to Exit...")

    if "_" not in display:
        game_end = True
        print("You win!")
        input("\nPress Enter to Exit...")

    print(stages[lives])
    print(f"{' '.join(display)}\n")