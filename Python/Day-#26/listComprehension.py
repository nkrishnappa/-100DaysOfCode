numbers = [1, 2, 3]
print(numbers) # [2, 3, 4]

new_list = []
for n in numbers:
    new_list.append(n+1)
print(new_list) # [2, 3, 4]

# Using List Comprehension - Integer
# [ new_item for item in lists ]
list_comp = [ num + 1 for num in numbers ]
print(list_comp) # [2, 3, 4]

name = "Nandisha"
new_list = [letter for letter in name]
print(new_list) # ['N', 'a', 'n', 'd', 'i', 's', 'h', 'a']


new_list = [ num * 2 for num in range(1,5)]
print(new_list) # [2, 4, 6, 8] 


# conditional List comprehensions
names = ["Manju", "Babu", "Nandisha", "Raj", "Dhanu"]
new_list = [name for name in names if len(name) < 5 ]
print(new_list) # ['Babu', 'Raj']

new_list = [ name.upper() for name in names if len(name) >= 5 ]
print(new_list) # ['MANJU', 'NANDISHA', 'DHANU']

