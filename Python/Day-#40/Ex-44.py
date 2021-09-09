import string

file_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\threeByThreeLettersInFiles.txt"
with open(file_path, "w") as file:
    for letter_1, letter_2, letter_3  in zip(string.ascii_uppercase[0::3], string.ascii_uppercase[1::3], string.ascii_uppercase[2::3]):
        file.write(letter_1 + letter_2 + letter_3 + "\n")