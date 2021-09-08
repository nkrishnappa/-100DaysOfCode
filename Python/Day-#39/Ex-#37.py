# Exercise 37 - Advanced Word Counter
"""
Question: Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that a comma can separate some words with no space. For example, "Hi, it's me." would need to be counted as three words. For your convenience, you can use the text file in the attachment.
"""

file_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#39\file.txt"


with open(file_path, "r") as file:
    contents = file.read().replace(",", " ").split(" ")

print(len(contents))