# Default Arguments
def my_fn(a, b, c=5):
    pass

my_fn(c=3, b=2, a=1)

# Unlimited Arguments
'''
# Problem
def add(a, b):
    print(a + b)

add(3,4) # 7
add(3, 4, 5) # TypeError: add() takes 2 positional arguments but 3 were given
'''

# Solution
def add(*args):
    """the add module will add any number of numbers
    Args:
    *args : numbers 
    """
    print(type(args)) # <class 'tuple'>
    sum = 0
    for element in args:
        sum += element
    print(sum)

add(3,4) # 7
add(3, 4, 5) # 12
add(3, 4, 5, 6, 7) # 25


# kwargs
def calculate(n, **kwargs):
    print(type(kwargs)) # <class 'dict'>
    # for key, value in kwargs.items():
    #     print(key,value)
    # add 3
    # multiply 5

    # print(kwargs["add"]) # 3

    # add additional argument n
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n) # 40


calculate(5, add=3, multiply=5)