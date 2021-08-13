############DEBUGGING#####################

# Describe Problem
# 1. for loop - will loop through till 19
# so print statement will never execute
'''
def my_function():
   for i in range(1, 20):
    if i == 20:
      print("You got it")
my_function()


#--------------------------------------------------
# solution 
#--------------------------------------------------
def my_function():
   for i in range(1,21):
    if i == 20:
      print("You got it")
my_function()
#--------------------------------------------------
'''

# Reproduce the Bug
# Issue will reproduce only when randint returns 6. randint returns random interger including 1, 6
# randint: (a: int, b: int) -> int
# Return random integer in range [a, b], including both end points.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num]) 

'''
# reproduce always
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#dice_num = randint(1, 6)
dice_num = 6
print(dice_imgs[dice_num])  # IndexError: list index out of range

#--------------------------------------------------
# solution 
#--------------------------------------------------
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, len(dice_imgs) - 1)
print(dice_imgs[dice_num]) 
#--------------------------------------------------
'''

# Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
'''
#--------------------------------------------------
# problem : 1994 will never execute
# solution : making changes to consider 1994 as Gen Z
#--------------------------------------------------
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")
#--------------------------------------------------
'''

# Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
'''
#--------------------------------------------------
# problem : 1. age is not a integer 2. indentation error 3. f-string is missing
# solution : indented print condition and age type casting to int
#--------------------------------------------------
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
#--------------------------------------------------
'''

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

'''
#--------------------------------------------------
# problem : == in input instruction, it return 0 
# solution : change == to =
#--------------------------------------------------
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(f"{pages}, {word_per_page}")
total_words = pages * word_per_page
print(total_words)
#--------------------------------------------------
'''

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
'''
#--------------------------------------------------
# problem : only mutate last item
# solution : append is running only after the for loop
#--------------------------------------------------
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
#--------------------------------------------------
'''