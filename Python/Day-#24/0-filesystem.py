'''
File System:
open, read, close
'''

"""
file = open("0_1-my_file.txt")
contents = file.read()
print(f"{contents}")
file.close()
"""

"""
# reading a file
with open("0_1-my_file.txt") as file:
    contents = file.read()
    print(contents)
"""

"""
# Write a file - over write 

with open("0_1-my_file.txt", "w") as file:
    file.write("I am over-writting\n")
    file.write("ohhh! Nooooo")
"""

# Write a file - append Mode
with open("0_1-my_file.txt", "a") as file:
    file.writelines("\nI am appending")
