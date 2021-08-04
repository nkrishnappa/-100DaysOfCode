'''
List is a data structure

syntax - 
variable = [items1, item2] 

- order will be retained
A list is an ordered and mutable Python container

'''

states_of_india = ["Karnataka", "AndraPradesh", "Kerala", "TamilNadu"]

states_of_india.append("MadyaPradesh")
states_of_india.extend(["Dehli", "Gujarat"])

print(states_of_india)
# ['Karnataka', 'AndraPradesh', 'Kerala', 'TamilNadu', 'MadyaPradesh', 'Dehli', 'Gujarat']

