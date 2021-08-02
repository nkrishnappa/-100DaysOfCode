# Write a program that adds the digits in a 2 digit number. 
# e.g. if the input was 35, then the output should be 3 + 5 = 8

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# validate the type
# isinstance(object, classtype)
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'list'>
# <class 'tuple'>
# <class 'dict'>
# <class 'set'>

sum = 0
if len(str(two_digit_number)) > 2 or isinstance(two_digit_number, int) == False:
    print ("""INPUT should be : 
        1. Size should be 2
        2. Type should be int 
    """)
    exit()

for n in str(two_digit_number):
    sum += int(n)
print (sum)

# TypeError: object of type 'int' has no len()
# if len(two_digit_number) > 2:
#     print ("Invalid Input. supported only of length 2")
#     exit()

# print (two_digit_number[0] + two_digit_number[1])
# TypeError: 'int' object is not subscriptable

