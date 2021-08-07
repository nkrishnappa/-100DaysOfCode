# Step 1 
import random
word_list = ["aardvark", "baboon", "camel", "tiger", "elephant"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# random_word = word_list[random.randint(0,len(word_list)-1)]
choosen_word = random.choice(word_list)

print(f"choosen word is {choosen_word}")

#TODO-2.1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for n in choosen_word:
    display.append("_")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter please : ").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
#TODO-2.2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]. 
for position in range(len(choosen_word)):
    if choosen_word[position] == guess:
        display[position] = guess

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)