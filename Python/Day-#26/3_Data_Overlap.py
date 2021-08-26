file_1 = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#26\3_1_file.txt"
file_2 = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#26\3_2_file.txt"

with open(file_1, "r") as file:
    file_1_contents = file.read().split()

with open(file_2, "r") as file:
    file_2_contents = file.read().split()

result = [int(element) for element in file_1_contents if element in file_2_contents]

# Write your code above 👆
print(result)
# [3, 6, 5, 33, 12, 7, 42, 13]