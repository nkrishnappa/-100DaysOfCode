import string

file_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\lettersInFiles.txt"
with open(file_path, "w") as file:
    # for letter in range(65,91):
    #     file.write(f"{chr(letter)}\n")
    for letter in string.ascii_uppercase:
        file.write(letter + "\n")