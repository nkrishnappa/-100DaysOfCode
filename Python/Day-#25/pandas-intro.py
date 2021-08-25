import pandas
# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/


data = pandas.read_csv("weather_data.csv")

# Exercise to conver celcius to  farenheit
monday = data[data.day == "Monday"]
"""
convert_to_f = (monday.temp * (9/5)) + 32 
print(convert_to_f)

0    53.6
Name: temp, dtype: float64
"""

"""
monday = data[data.day == "Monday"]
print(monday)
      day  temp condition
0  Monday    12     Sunny
"""


"""
print(monday.condition)

0    Sunny
Name: condition, dtype: object
"""

# Excercise : Get the max temparature day of the week 
"""
print (data[data.temp == data.temp.max()])
      day  temp condition
6  Sunday    24     Sunny
"""

# Get data in ROW
"""
print (data[data.day == "Monday"])
      day  temp condition
0  Monday    12     Sunny
"""

# print(data.columns) # Index(['day', 'temp', 'condition'], dtype='object')
# print(data.condition) # or print(data["condition"])
"""
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
"""



"""
0     Sunny
1      Rain
2      Rain
3    Cloudy
4     Sunny
5     Sunny
6     Sunny
Name: condition, dtype: object
"""

"""
# find avarage temperature
temperature_sum = data["temp"].sum()
temperature_average = temperature_sum / len(data["temp"])

print(round(temperature_average, 2)) # 17.43
# series functions
print(round(data["temp"].mean(), 2)) # 17.43
print(data["temp"].max()) # 24

data_list = data["temp"].to_list()
"""

"""
print(data_list)
[12, 14, 15, 14, 21, 22, 24]
"""

data_dict = data.to_dict()
"""
print(data_dict)
{'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4:
'Sunny', 5: 'Sunny', 6: 'Sunny'}}
"""

# print(type(data))           # <class 'pandas.core.frame.DataFrame'>
# print(type(data["temp"]))   # <class 'pandas.core.series.Series'>

"""
print(data)

         day  temp condition
0     Monday    12     Sunny
1    Tuesday    14      Rain
2  Wednesday    15      Rain
3   Thursday    14    Cloudy
4     Friday    21     Sunny
5   Saturday    22     Sunny
6     Sunday    24     Sunny

"""

"""
print(data["temp"])
0    12
1    14
2    15
3    14
4    21
5    22
6    24
Name: temp, dtype: int64
"""




