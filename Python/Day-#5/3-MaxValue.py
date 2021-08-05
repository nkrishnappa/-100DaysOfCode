'''
write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91
'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
if not student_scores:
    print("Provided Empty list ...")
else:
    highest_score = 0
    for n in range(0, len(student_scores) - 2):
        if student_scores[n] > student_scores[n+1]:
            highest_score = student_scores[n]
        else:
            highest_score = student_scores[n+1]
    print(f"The highest score in the class is {highest_score}")

    highest_score = 0
    for student_score in student_scores:
        if highest_score < student_score:
            highest_score = student_score
    print(f"The highest score in the class is {highest_score}")