print("Welcome to the Rollercoaster")
height = int(input("What is the height in cms? "))

if height > 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Pay - $5")
    elif age < 18:
        print("Pay - $12")
    elif age > 18:
        print("Pay - $10")  
else:
    print("You have to grow before you can take a ride")
