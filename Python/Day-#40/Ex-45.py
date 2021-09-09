# Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b, and so on

import string
FILE_PATH = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\Ex-45"
for letter in string.ascii_uppercase:
    file_name = FILE_PATH + f"/{letter}.txt"
    with open(file_name, "w")as file:
        file.write(letter)