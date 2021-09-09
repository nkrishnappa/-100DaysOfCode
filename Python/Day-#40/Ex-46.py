# Write a script to extract the 26 letters from the file and add it to the list


# import string
# FILE_PATH = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\Ex-45"
# extract_letter = []
# for letter in string.ascii_uppercase:
#     file_name = FILE_PATH + f"/{letter}.txt"
#     with open(file_name, "r")as file:
#         extract_letter.append(file.read())

# print(extract_letter)

import glob
FILE_PATH = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\Ex-45"
extract_letter = []
for file in glob.glob(f"{FILE_PATH}\*.txt"):
    with open(file, "r") as f:
       extract_letter.append(f.read())

print(extract_letter)


# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']