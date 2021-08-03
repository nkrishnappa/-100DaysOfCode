"""
write a program that tests the compatibility between two people. 
We're going to use the super scientific method recommended by BuzzFeed.

To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.


For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

name1 = name1.lower()
name2 = name2.lower()
combined = name1 + name2

true = combined.count("t") + combined.count("r") + combined.count("u") + combined.count("e")
love = combined.count("l") + combined.count("o") + combined.count("v") + combined.count("e")

loveScore = int(str(true) + str(love))

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together") 
else:
    print(f"Your score is {loveScore}")
