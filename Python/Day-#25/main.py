
# with open(r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\weather_data.csv", "r") as weather_data:
#     print(weather_data.readlines())

"""
import csv
with open(r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\weather_data.csv", "r") as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    # print(data) # <_csv.reader object at 0x01083F78>
    for row in data:
        # print(row)
        try:
            temperature.append(int(row[1]))
        except ValueError:
            pass
    print(temperature)
"""

"""
print(row)

['day', 'temp', 'condition']
['Monday', '12', 'Sunny']
['Tuesday', '14', 'Rain']
['Wednesday', '15', 'Rain']
['Thursday', '14', 'Cloudy']
['Friday', '21', 'Sunny']
['Saturday', '22', 'Sunny']
['Sunday', '24', 'Sunny']

"""

