import random
# syntax
# new_dict = {new_key:new_value for item in list}
# new_dict = { new_key:new_value for key,value in dict.items() if test}

names = ["Manju", "Babu", "Nandisha", "Raj", "Dhanu", "Naveen"]
students_score = {student:random.randint(1,100) for student in names }
print(students_score)

# passed_students = { key:value for key,value in dict.items(students_score) if value >= 35}
passed_students = { student:score for student,score in students_score.items() if score >= 35}
print(passed_students)
# {'Manju': 41, 'Babu': 59, 'Nandisha': 86, 'Raj': 97, 'Dhanu': 26, 'Naveen': 52}
# {'Manju': 41, 'Babu': 59, 'Nandisha': 86, 'Raj': 97, 'Naveen': 52}