'''
BlackJack
'''
from art import logo
import os
import random
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

GAME_OVER = False

def draw_a_card(player, count: int) -> None:
    global GAME_OVER
    if player == "user":
        deck = user_choice_List
    else:
        deck = computer_choice_List

    while count > 0:
        selected_card = random.choice(cards)
        deck.append(selected_card)
    
        if 11 in deck and sum(deck) > 21:
            deck.remove(11)
            deck.append(1)

        if player == "computer" and sum(computer_choice_List) > 21:
            computer_choice_List.pop()
        elif player == "user":
            if sum(user_choice_List) > 21:
                GAME_OVER = True
                print_status(False)
                print("You went over. You lose 😤")
                return
        
        if 11 in deck and 10 in deck and len(deck) == 2:
            print(f"{player.upper()} has Blackjack - {deck}")
            print("You Win!")
            GAME_OVER = True
            return
        count -= 1

def print_status(is_hide):
    if is_hide == True:
        current_score = sum(user_choice_List)
        print(f"\t Your cards: {user_choice_List}, current score: {current_score}")
        print(f"\t Computer's first card: {computer_choice_List[0]}")
    elif is_hide == False:
        user_current_score = sum(user_choice_List)
        computer_current_score = sum(computer_choice_List)        
        print(f"\t Your final hand: {user_choice_List}, current score: {user_current_score}")
        print(f"\t Computer's final hand: {computer_choice_List}, current score: {computer_current_score}")

def check_the_winner():
    user_current_score = sum(user_choice_List)
    computer_current_score = sum(computer_choice_List)
    
    print_status(False)
    if user_current_score == computer_current_score:
        print(f"Draw!")
    elif (not user_current_score > 21) and user_current_score > computer_current_score:
        print(f"You Win!")
    else:
        print(f"You Lose")

exit_condition = False
while exit_condition == False:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice == "y":
        condition_to_exit = False
        GAME_OVER = False
        computer_choice_List = []
        user_choice_List = []
        
        os.system("clear")
        print(logo)
        
        draw_a_card("user",2)
        if GAME_OVER == True:
            condition_to_exit = True
            break

        draw_a_card("computer", 2)
        if GAME_OVER == True:
            condition_to_exit = True
        
        while condition_to_exit == False:
            print_status(True)
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "n" :
                condition_to_exit = True
                check_the_winner()
            elif choice == "y":
                draw_a_card("computer", 1)
                draw_a_card("user",1)
            if GAME_OVER == True:
                condition_to_exit = True
                
    elif choice == "n":
        print("GoodBye")
        exit_condition = True
