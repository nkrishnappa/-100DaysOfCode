# KeyError
# a_dic = {
#     "key" : "value"
# }

# a_dic["key1"] # KeyError: 'key1'

# IndexError

# TypeError

# FileNotFound
"""
a_dic = {
    "key" : "value"
}
try:
    file = open("file.txt", "r")
    file.read()
    a_dic["key1"] # KeyError: 'key1'

except FileNotFoundError:
    file = open("file.txt", "w")
    print(f"Hiii")
except KeyError as error:
    print(f"The key not found : {error}") # The key not found : 'key1'
else:
    print(f"Found File file.txt")
finally:
    print("Finally")
    file.close()
"""
"""
# raise your own Exception
a_dic = {
    "key" : "value"
}
try:
    file = open("file.txt", "r")
    file.read()
    a_dic["key1"] # KeyError: 'key1'

except FileNotFoundError:
    file = open("file.txt", "w")
    print(f"Hiii")
except KeyError as error:
    print(f"The key not found : {error}") # The key not found : 'key1'
else:
    print(f"Found File file.txt")
finally:
    raise TypeError("This is user defined error")
    # print("Finally")
    # file.close()
"""

