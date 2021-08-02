"""
Welcome to the tip calculator.

What was the total bill? $124.56
What percentage tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7
Each person should pay: $19.93

#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
"""

def tipCalculator(noOfPeople, amount, tip):
    return round( (float(amount) / int(noOfPeople)) * (1 + int(tip)/100) ,2)

if __name__ == "__main__":
    print ("Welcome to the tip calculator.")
    amount = input("What was the total bill? $")
    tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
    noOfPeople = input("How many people to split the bill? ")
    print(f"Each person should pay: {tipCalculator(noOfPeople, amount, tip)}")