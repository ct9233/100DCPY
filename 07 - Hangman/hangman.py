import random

stages = [
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
    """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
]
word_list = ["aardvark", "barracuda", "cheetah"]
chosen_word = random.choice(word_list)

lives = 6
game_end = False
display = []

for letter in chosen_word:
    display.append("_")

print("Welcome to Hangman!")
print(stages[lives])
print(f"{' '.join(display)}\n")

while not game_end:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
    if guess not in display:
        lives -= 1
        if lives == 0:
                game_end = True
                print("You lose.")

    if "_" not in display:
        game_end = True
        print("You win!")

    print(stages[lives])
    print(f"{' '.join(display)}\n")