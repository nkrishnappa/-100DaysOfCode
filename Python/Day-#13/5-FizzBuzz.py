# for number in range(1, 101):
#   if number % 3 == 0 or number % 5 == 0:
#     print("FizzBuzz")
#   if number % 3 == 0:
#     print("Fizz")
#   if number % 5 == 0:
#     print("Buzz")
#   else:
#     print([number])

'''
--------------------------------------------------
problem : 
    1. We are printing the number when number not divisible by 5
    2. FizzBuzz should be print when both conditions match (divisible by 3 and 5) 
    3. if elif else not properly aligned 
solution : 
    1. use "AND" operation instead of the "OR"
    2. reconstruct the if elif else blocks  
--------------------------------------------------
'''

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print([number])