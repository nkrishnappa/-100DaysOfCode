'''

write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Example Input
Angela, Ben, Jenny, Michael, Chloe

Example Output
Michael is going to buy the meal today!

'''

import random
# 🚨 Don't change the code below 👇
# Split string method
namesAsCSV = input("Give me everybody's names, seperated by a comma. ")
names = namesAsCSV.split(", ")

random_choice = random.randint(0, len(names)-1)
print (f"{names[random_choice]} is going to buy the meal today!")

random_choice = random.choice(names)
print (f"{random_choice} is going to buy the meal today!")

# Give me everybody's names, seperated by a comma. Nandisha, Chandhu, Bhavanika
# Chandhu is going to buy the meal today!