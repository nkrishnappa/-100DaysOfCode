import pandas
import json

file_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#26\NATO-alphabet-start\nato_phonetic_alphabet.csv"

#TODO 1. Create a dictionary in this format:
read_file = pandas.read_csv(file_path)
# nato_alpha_dictionary = read_file.to_dict() 

# nato_alpha_dictionary = {}
# for index, row in read_file.iterrows():
#     nato_alpha_dictionary[row.letter] = row.code

nato_alpha_dictionary = { row.letter:row.code for index, row in read_file.iterrows()}
# print(json.dumps(nato_alpha_dictionary, indent=2))

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word : ")
phonetic_code_list = [ nato_alpha_dictionary[letter.upper()] for letter in word if letter.isalpha() ]

print(phonetic_code_list) # ['November', 'Alfa', 'November', 'Delta', 'India', 'Sierra', 'Hotel', 'Alfa']
"""
print(json.dumps(nato_alpha_dictionary, indent=2))
{
  "A": "Alfa",
  "B": "Bravo",
  "C": "Charlie",
  "D": "Delta",
  "E": "Echo",
  "F": "Foxtrot",
  "G": "Golf",
  "H": "Hotel",
  "I": "India",
  "J": "Juliet",
  "K": "Kilo",
  "L": "Lima",
  "M": "Mike",
  "N": "November",
  "O": "Oscar",
  "P": "Papa",
  "Q": "Quebec",
  "R": "Romeo",
  "S": "Sierra",
  "T": "Tango",
  "U": "Uniform",
  "V": "Victor",
  "W": "Whiskey",
  "X": "X-ray",
  "Y": "Yankee",
  "Z": "Zulu"
}
"""

