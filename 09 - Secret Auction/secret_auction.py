import os
from art import logo

bid_tracking = []
continue_bidding = True

print(logo)
print("Welcome to the bidding for the secret auction!\n")

while continue_bidding == True:
    bidder_name = input("Enter your name: ")
    bid_amount = input("Enter the bid amount: $")

    bid_instance = {}
    bid_instance["name"] = bidder_name
    bid_instance["bid"] = bid_amount

    bid_tracking.append(bid_instance)

    more_bidders = input("Are there any more bidders in the auction?  Please type 'yes' or 'no': ")
    if more_bidders == "no":
        continue_bidding = False
    else:
        os.system("cls")

# print(f"{bid_tracking[0]['bid']}")

highest_bid = 0
winner = ""
for each in bid_tracking:
    this_bid = int(bid_tracking[bid_tracking.index(each)]["bid"])
    if this_bid > highest_bid:
        highest_bid = this_bid
        winner = bid_tracking[bid_tracking.index(each)]["name"]

print(f"\nThe winner of the auction is {winner} with the high bid of ${highest_bid}.")
input("\nPress Enter to exit...")