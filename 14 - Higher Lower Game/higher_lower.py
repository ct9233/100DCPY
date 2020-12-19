import random
import os
from art import logo, vs
from game_data import data

game_continues = True
compare_a = ""
compare_b = ""
index_a = int
index_b = int
score = 0

while game_continues == True:
    index_a = index_a if compare_a != "" else random.randrange(0, len(data))
    index_b = random.randrange(0, len(data))
    while index_b == index_a:
        index_b = random.randrange(0, len(data))
    compare_a = compare_a if compare_a != "" else data[index_a]
    compare_b = data[index_b]

    print(logo)
    if score > 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}.")
    print(vs)
    print(f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}.")
    player_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    opposite = "b" if player_choice == "a" else "a"
    player_value = "compare_" + player_choice + "['follower_count']"
    opposing_value = "compare_" + opposite + "['follower_count']"

    os.system("cls")

    if eval(player_value) > eval(opposing_value):
        score += 1
        compare_a = data[index_b]
        index_a = index_b
    else:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        game_continues = False

input("\nPress Enter to exit...")
