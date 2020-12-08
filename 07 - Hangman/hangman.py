import random

word_list = ["aardvark", "barracuda", "cheetah"]
chosen_word = random.choice(word_list)

display = []
for letter in chosen_word:
    display.append("_")
print(display)

while "_" in display:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            print("Right")
            display[position] = guess
        else:
            print("Wrong")
    print(display)

print("You win!")