import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def make_a_guess(number: int, attempts: int):
    successfully_matched = False
    while successfully_matched == False and attempts > 0:
        print(f"You have {attempts} remaining to guess the numer.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}")
            successfully_matched = True
            return
        elif guess > number:
            print("Too High")
        elif guess < number:
            print(f"Too Small")
        
        print("Guess again.")
        attempts -= 1
    
    if attempts == 0:
        print("You've run out of guesses, you lose")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif level == "hard":
        return HARD_LEVEL_ATTEMPTS
    
print(logo)
print("Welcome to the Number Game!")
print("I'm thinking of a number  between 1 and 100.")
choosen_number = random.randint(1,101)
alloted_attempts = set_difficulty()
make_a_guess(number=choosen_number, attempts=alloted_attempts)