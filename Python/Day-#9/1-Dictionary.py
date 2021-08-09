'''
Defination:
    Dictionary in Python is an ordered collection of data values, used to store data values like a map, 
    which, unlike other Data Types that hold only a single value as an element, Dictionary holds key:value pair. 
    Key-value is provided in the dictionary to make it more optimized.
Syntax:
    nameOfTheDictionary = {}
    nameOfTheDictionary = {
        Key : value,
        ...
    }
Errors : 
    KeyError
'''
# create a empty dictionary
programming_dictionary = {}
programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected",
    "Function" : "A piece of code that you ca easilu call over and over again",
    "Loop" : "The action of doing something over and over again"
}

print(programming_dictionary["Bug"])

# Edit the item in the dictionary 
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through the dictionary
for key,value in programming_dictionary.items():
    print(key,value)