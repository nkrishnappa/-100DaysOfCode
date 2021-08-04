'''
https://wrpsa.com/the-official-rules-of-rock-paper-scissors/

The outcome of the game is determined by 3 simple rules:
Rock wins against scissors.
Scissors win against paper.
Paper wins against rock.

'''
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_choices = [rock, paper, scissors]
your_choice = int(input("what fo you choose? type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
print (list_choices[your_choice])

print("Computer chose:\n")
computer_choice = random.randint(0,2)
print (list_choices[computer_choice])

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock. 

if (your_choice == computer_choice):
    print("Draw")
elif (your_choice == 0 and computer_choice == 2) or (your_choice == 1 and computer_choice == 0)  or (your_choice == 2 and computer_choice == 1):
    print("You win!")
else:
    print("You lose!")

# solution #2
# rock 0 > scissors 2
# scissors 2 > paper 1
# paper 1 > rock 0

# 0 > 2 , 1 > 0 , 2 > 1
if (your_choice == computer_choice ):
    print("Draw")
elif (your_choice == 0 and computer_choice == 2):
    print("You win!")
elif (your_choice == 2 and computer_choice == 0):
    print("You lose!")
elif computer_choice > your_choice:
    print("You lose!")
elif computer_choice < your_choice:
    print("You win!")
