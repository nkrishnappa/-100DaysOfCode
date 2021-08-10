from art import logo
import os

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

def calculate(first: int, second: int, op: str) -> int:
    print(f"{first} {op} {second} = {op}")
    return f"first op second"

operations = {
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide
    }

def calculator():
    os.system("clear")
    print(logo)
    continue_operation = True
    first_number = float(input("What's the first number?: "))
    while continue_operation == True:
        print(" \n".join({key for key in operations}))
        operation_symbol = input("Pick an operation : ")
        second_number = float(input("What's the next number?: "))

        calculationFunction = operations[operation_symbol] 
        answer = calculationFunction(first_number, second_number)

        print(f"{first_number} {operation_symbol} {second_number} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' start a new calculations . : ")
        if choice == 'n':
            continue_operation = False
            calculator()
        first_number = answer

calculator()