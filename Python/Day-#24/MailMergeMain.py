# $ find Input/
# Input/
# Input/Letters
# Input/Letters/starting_letter.txt
# Input/Names
# Input/Names/Invited_names.txt

# nkrishnappa@nkrishnappa-inl MINGW64 Day-#24 (master)
# $ find Output/
# Output/
# Output/ReadyToSend


# TODO: Create a letter using starting_letter.txt 
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import re

letter = ""
senders_names_list = []
with open("./Input/Names/Invited_names.txt") as invited_file:
    # senders_names_list = invited_file.readlines()
    senders_names_list = invited_file.read().split("\n")

for sender in senders_names_list:
    if sender:
        with open("./Input/Letters/starting_letter.txt") as start_letter_file:
            mail_contents = start_letter_file.read().replace("[name]", sender.strip()) # strip is not required while using split
            with open(f"./Output/ReadyToSend/letter_for_{sender.strip().capitalize()}.txt", "w") as output:
                output.write(mail_contents)