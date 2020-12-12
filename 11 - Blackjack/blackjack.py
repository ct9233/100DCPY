import os
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

round_continues = False

print("\nWelcome to Blackjack!")


def blackjack_round():
    os.system("cls")
    print(logo)

    user_cards = []
    computer_cards = []

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    if user_score == 21:
        print(f"Player cards: {user_cards}.  Blackjack! Player wins!")
        play_again = input("Play again?  Type 'y' or 'n': ")
        if play_again == "y":
            blackjack_round()
        else:
            return
    elif computer_score == 21:
        print(f"Computer cards: {computer_cards}.  Blackjack! Computer wins!")
        play_again = input("Play again?  Type 'y' or 'n': ")
        if play_again == "y":
            blackjack_round()
        else:
            return
    else:
        round_continues = True

    print(f"\nComputer's first card: {computer_cards[0]}")

    while round_continues:
        print(f"\nPlayers cards: {user_cards}, current score: {user_score}")
        player_hit = input("Type 'y' to get another card, or type 'n' to hold: ")


play_game = input("\nWould you like to start a round of Blackjack? (type 'y' or 'n'): ")

if play_game == "y":
    blackjack_round()


input("\nPress Enter to exit...")