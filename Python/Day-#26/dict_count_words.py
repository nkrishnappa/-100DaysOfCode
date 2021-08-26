# Dictionary Comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
result = { word:len(word) for word in sentence.split()}

# Write your code below:
print(result)
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

import json
print(json.dumps(result,indent=2)) 
# {
#   "What": 4,
#   "is": 2,
#   "the": 3,
#   "Airspeed": 8,
#   "Velocity": 8,
#   "of": 2,
#   "an": 2,
#   "Unladen": 7,
#   "Swallow?": 8
# }