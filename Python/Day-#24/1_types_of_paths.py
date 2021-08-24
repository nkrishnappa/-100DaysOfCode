"""
1. Absolute File path - /root/filename.extension
2. Relative File path - filename.extension or ./filename.extension

# How to goto the parent folder - ../

"""

# Using Absolute file path
with open(r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#24\FindMeDude\my_file.txt") as file:
    print(file.read())

# relative file path
with open(r"./FindMeDude/my_file.txt") as file:
    print(file.read())

with open(r"../Day-#24/FindMeDude/my_file.txt") as file:
    print(file.read())