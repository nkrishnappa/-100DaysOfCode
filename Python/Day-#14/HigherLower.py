from art import logo, vs
from game_data import data
import random
import os

def display(player1:list, player2:list) -> None:
    print(f"Compare A: {player1['name']}, a {player1['description']}, from {player1['country']}")
    print(vs)
    print(f"Against B: {player2['name']}, a {player2['description']}, from {player2['country']}")

def compare(player1: dict, player2: dict, guess: str) -> bool:
    if player1['follower_count'] > player2['follower_count']:
        return guess == "A"
    else:
        return guess == "B"

def clear_my_screen():
    os.system("clear")
    print(logo)

clear_my_screen()
random_person_1 = random.choice(data)
count_streak = 0
is_more_followers = True

while is_more_followers == True:
    random_person_2 = random.choice(data)
    if random_person_2 == random_person_1:
        random_person_2 = random.choice(data)
    display(player1=random_person_1, player2=random_person_2)

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()
    is_more_followers = compare(player1=random_person_1, player2=random_person_2, guess=guess)

    if is_more_followers:
        count_streak += 1
        clear_my_screen()
        print(f"You're right! Currnet score: {count_streak}")
        if guess == "A":
            random_person_1 = random_person_2  
    else:
        clear_my_screen()
        print(f"Sorry, that's wrong. Final score: {count_streak}")