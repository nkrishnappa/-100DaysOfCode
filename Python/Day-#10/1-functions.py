'''
A function is a block of code that only runs when it is called. 
Python functions return a value using a return statement, 
if one is specified. 
A function can be called anywhere after the function has been declared. 
By itself, a function does nothing.
'''

def format_name(first_name: str, last_name: str) -> str:
    if first_name == "" or last_name == "":
        return
    formated_first_name = first_name.title()
    formated_last_name = last_name.title()
    return f"{formated_first_name} {formated_last_name}"

first_name_input = input("What's your first name? ")
last_name_input = input("What's your last name? ")
print(first_name_input, last_name_input)
# print(format_name("NandishA", "KrishNappa"))