import os
from art import logo

print(logo)

bidding_dictionary = []
want_to_add_more = True

def updateMyDictionary(name: str, bid_price: int) -> None:
    new_dictionary = {
        "name" : name,
        "bid" : bid_price,
        }
    bidding_dictionary.append(new_dictionary)

def declare_winner():
    winner = []
    maxbid = 0
    for value in bidding_dictionary:
        if value["bid"] > maxbid:
            maxbid = value["bid"]
            winner.append(value["name"])
        elif value["bid"] == maxbid:
            winner.append(value["name"])
    winners = " ".join(winner)
    print(f'{winners} is/are the winner(s) with bid price {maxbid}')

while want_to_add_more == True:
    name = input("What is your name? ")
    bid_price = int(input("What's your bid?: $"))

    updateMyDictionary(name, bid_price)
    choice = input("Are there any bidders in the room? yes/no? ")
    if choice == "no":
        want_to_add_more = False
        declare_winner()
    else:
        os.system("clear")

print("Goodbye..")
