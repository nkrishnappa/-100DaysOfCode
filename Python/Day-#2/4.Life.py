"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
It will take your current age as the input and output a message with our time left in this format:
You have x days, y weeks, and z months left.
Where x, y and z are replaced with the actual calculated numbers.


# There are 365 days in a year, 52 weeks in a year and 12 months in a year.
# OUTPUT - You have 12410 days, 1768 weeks, and 408 months left.
"""

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days, weeks, months = 0, 0, 0
years_remaining = 90 - int(age) 
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12

print (f"You have {days} days, {weeks} weeks, and {months} months left.")