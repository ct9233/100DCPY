import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

player_choice = int(input("Welcome to Rock, Paper, Scissors!\n\nType 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)

computer_choice = random.randint(0, 2)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if player_choice == computer_choice:
    print("The game is a draw.")
elif player_choice == 0:
    if computer_choice == 1:
        print("The computer wins!")
    else:
        print("You win!")
elif player_choice == 1:
    if computer_choice == 2:
        print("The computer wins!")
    else:
        print("You win!")
elif player_choice == 2:
    if computer_choice == 0:
        print("The computer wins!")
    else:
        print("You win!")
else:
    print("You choice was invalid! You lose!")
input("\nPress Enter to Exit...")