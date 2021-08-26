student_dict = {
    "student" : ["Manju", "Babu", "Nandisha", "Raj", "Dhanu", "Naveen"],
    "scores" : [40, 50, 80, 20, 50, 90 ]
}

# looping through dictionaries
# for key, value in student_dict.items():
#     print(key,value)
# student ['Manju', 'Babu', 'Nandisha', 'Raj', 'Dhanu', 'Naveen']
# scores [40, 50, 80, 20, 50, 90]

import pandas

student_data_frame = pandas.DataFrame(student_dict)
for index, row in student_data_frame.iterrows():
    # print(index) # 0 - 5 it prints 
    # print(row)
    # print(row.scores) 
    print(row.student)

"""
print(row.student)
Manju
Babu
Nandisha
Raj
Dhanu
Naveen
"""

"""
print(row.scores) 
40
50
80
20
50
90
"""

"""
print(row) 
student    Manju
scores        40
Name: 0, dtype: object
student    Babu
scores       50
Name: 1, dtype: object
student    Nandisha
scores           80
Name: 2, dtype: object
student    Raj
scores      20
Name: 3, dtype: object
student    Dhanu
scores        50
Name: 4, dtype: object
student    Naveen
scores         90
Name: 5, dtype: object
"""


"""
print(student_data_frame)

    student  scores
0     Manju      40
1      Babu      50
2  Nandisha      80
3       Raj      20
4     Dhanu      50
5    Naveen      90
"""

# looping through DataFrames
"""
for key, value in student_data_frame.items():
    print(key,value)

student 0       Manju
1        Babu
2    Nandisha
3         Raj
4       Dhanu
5      Naveen
Name: student, dtype: object
scores 0    40
1    50
2    80
3    20
4    50
5    90
Name: scores, dtype: int64
"""
