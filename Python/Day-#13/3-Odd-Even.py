'''
Instructions:
    Read this the code in main.py
    Spot the problems 🐞.
    Modify the code to fix the program.

Fix the code so that it works and passes the tests when you submit.

code :
number = int(input("Which number do you want to check?"))
if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
'''
#--------------------------------------------------
# problem : In if condition, we are using the assignment operator 
# solution : change = to ==
#--------------------------------------------------
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
