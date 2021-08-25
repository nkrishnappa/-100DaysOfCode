import pandas

# Create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "Nandisha", "Chand"],
    "scores" : [76, 56, 65] 
}

data = pandas.DataFrame(data_dict)
"""
print(data)
   students  scores
0       Amy      76
1  Nandisha      56
2     Chand      65
"""
# convert dict to csv
data.to_csv("student.csv")

"""
$ cat student.csv
,students,scores
0,Amy,76
1,Nandisha,56
2,Chand,65

"""
