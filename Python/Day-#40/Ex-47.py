# Write a script to extract the 26 letters from the file and add it to the list only if that letter is in PYTHON


import glob
FILE_PATH = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#40\Ex-45"
extract_letter = []
for file in glob.glob(f"{FILE_PATH}\*.txt"):
    with open(file, "r") as f:
        content = f.read()
        if content in "PYTHON":
            extract_letter.append(content)

print(extract_letter)
# ['H', 'N', 'O', 'P', 'T', 'Y']
