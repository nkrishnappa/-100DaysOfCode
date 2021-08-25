import pandas

data = pandas.read_csv(r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#25\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
my_census_dictionary = {
    'Fur Color' : [],
    'Count' : []
}

list_of_colors = []
for color in data['Primary Fur Color'].unique():
    if str(color) != 'nan':
        list_of_colors.append(color)
        my_census_dictionary['Fur Color'].append(color)
        count_color = data[data['Primary Fur Color'] == color]
        my_census_dictionary['Count'].append(count_color.shape[0])

# print(my_census_dictionary)
# {'Fur Color': ['Gray', 'Cinnamon', 'Black'], 'Count': [2473, 392, 103]}

data_dict = pandas.DataFrame(my_census_dictionary)
data_dict.to_csv("squirrel_color.csv")

# ,Fur Color,Count
# 0,Gray,2473
# 1,Cinnamon,392
# 2,Black,103