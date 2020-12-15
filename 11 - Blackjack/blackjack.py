import os
import sys
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print("\nWelcome to Blackjack!")


def another_round():
    play_again = input("Play again?  Type 'y' or 'n': ")
    if play_again == "y":
        blackjack_round()
    else:
        print("\nGoodbye!")
        input("\nPress Enter to exit...")


def blackjack_round():
    os.system("cls")
    print(logo)

    user_cards = []
    computer_cards = []
    round_continues = True

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    if sum(user_cards) == 22:
        user_cards[1] = 1
    if sum(computer_cards) == 22:
        computer_cards[1] = 1

    print(f"\nComputer's first card: {computer_cards[0]}")

    while round_continues:
        if sum(user_cards) == 21:
            print(f"\nPlayer cards: {user_cards}.  Blackjack! Player wins!\n")
            round_continues = False
            another_round()
        elif sum(computer_cards) == 21:
            print(f"\nComputer cards: {computer_cards}.  Blackjack! Computer wins!\n")
            round_continues = False
            another_round()
        else:
            print(f"\nPlayers cards: {user_cards}, current score: {sum(user_cards)}")
            player_hit = input("Type 'y' to get another card, or type 'n' to hold: ")

            if player_hit == "y":
                user_cards.append(random.choice(cards))
                if sum(user_cards) > 21:
                    if 11 in user_cards:
                        user_cards = [1 if x == 11 else x for x in user_cards]
                    else:
                        print(f"\nPlayer cards: {user_cards}.  Score: {sum(user_cards)}  Bust! Player lost.\n")
                        round_continues = False
                        another_round()
            else:
                while sum(computer_cards) < 16:
                    computer_cards.append(random.choice(cards))
                    if sum(computer_cards) > 21 and 11 in computer_cards:
                        computer_cards = [1 if x == 11 else x for x in computer_cards]
                if sum(computer_cards) > 21:
                    print(f"\nComputer cards: {computer_cards}.  Score: {sum(computer_cards)}  Bust! Computer lost.\n")
                    round_continues = False
                    another_round()
                elif sum(computer_cards) == 21:
                    print(
                        f"\nComputer cards: {computer_cards}.  Score: {sum(computer_cards)}  Blackjack! Computer wins!\n"
                    )
                    round_continues = False
                    another_round()
                elif sum(computer_cards) > sum(user_cards):
                    print(
                        f"\nComputer cards: {computer_cards}.  Score: {sum(computer_cards)}\nPlayer cards: {user_cards}.  Score: {sum(user_cards)}\nComputer wins!\n"
                    )
                    round_continues = False
                    another_round()
                elif sum(computer_cards) < sum(user_cards):
                    print(
                        f"\nComputer cards: {computer_cards}.  Score: {sum(computer_cards)}\nPlayer cards: {user_cards}.  Score: {sum(user_cards)}\nPlayer wins!\n"
                    )
                    round_continues = False
                    another_round()
                elif sum(computer_cards) == sum(user_cards):
                    print(
                        f"\nComputer cards: {computer_cards}.  Score: {sum(computer_cards)}\nPlayer cards: {user_cards}.  Score: {sum(user_cards)}\nIt's a draw!\n"
                    )
                    round_continues = False
                    another_round()


play_game = input("\nWould you like to start a round of Blackjack? (type 'y' or 'n'): ")

if play_game == "y":
    blackjack_round()
else:
    input("\nPress Enter to exit...")