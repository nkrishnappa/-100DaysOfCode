'''
Nested functions
Higher Order  functions


'''

def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

# Higher Orfer function
def calculator(n1, n2, func):
    return func(n1, n2)
print(f"{calculator(2,3,add)}")