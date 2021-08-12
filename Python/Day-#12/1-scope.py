'''
Scope
    Global Scope
    Local Scope

Tip : Avoid Modifying the Global scope
      make use of the "return"

Remember that in Python there is no block scope. Inside a if/else/for/while code block is the same as outside it.

'''
# Global Scope
player_age = 15

def player_rah_age():
    # Local Scope
    player_age = 20
    print(f"inside the function : {player_age}")

player_rah_age()
print(f"Outside the function : {player_age}")

"""
inside the function : 20
Outside the function : 15
"""

# Modifying the Global scope
def player():
    global player_age
    player_age = 20
    print(f"inside the function : {player_age}")

player()
print(f"Outside the function : {player_age}")
'''
inside the function : 20
Outside the function : 20
'''

# using return 
player_age = 25

def player():
    # Tip use the return functions - global player_age
    print(f"inside the function : {player_age}")
    return player_age + 20

player()
print(f"Outside the function : {player_age}")
'''
inside the function : 20
Outside the function : 20
'''



# Global Constants
