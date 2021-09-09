"""

Question: Create a script that generates a file where all letters of the English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.

"""
import string

file_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\twoByTwoLettersInFiles.txt"
with open(file_path, "w") as file:
    # for letter_1, letter_2  in zip(string.ascii_uppercase[0::2], string.ascii_uppercase[1::2]):
    #     file.write(letter_1 + letter_2 + "\n")
    for letter_1, letter_2 in zip(range(65,91,2), range(66,91,2)):
        file.write(chr(letter_1) + chr(letter_2) + "\n")
