# Prime Number - The number which only divisible by itself and 1

"""
https://en.wikipedia.org/wiki/Prime_number

You need to write a function that checks whether if the number passed into it is a prime number or not.
e.g. 2 is a prime number because it's only divisible by 1 and 2.

But 4 is not a prime number because you can divide it by 1, 2 or 4.

Example Input 1
73
Example Output 1
It's a prime number.

Example Input 2
75
Example Output 2
It's not a prime number.

"""
# brute-force 
# def prime_checker(number: int) -> bool:
#     for num in range(2, number):
#         if number % num == 0:
#             print("It's not a prime number.")
#             return False
#     print("It's a prime number")
#     return True

# Improve
'''
If a number n is not a prime, it can be factored into two factors a and b:
n = a * b

Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n.
So in any factorization of n, at least one of the factors must be smaller than the square root of n, 
and if we can't find any factors less than or equal to the square root, n must be a prime.

'''
import math
def prime_checker(number: int) -> bool:
    for num in range(2, math.ceil(math.sqrt(number))+1):
        if number % num == 0:
            print("It's not a prime number.")
            return False
    print("It's a prime number")
    return True

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
