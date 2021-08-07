import random
from hangman_words import word_list
from hangman_logo import stages, logo 

#TODO-5.1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
#word_list = ["aardvark", "baboon", "camel"]

#TODO-1.1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# random_word = word_list[random.randint(0,len(word_list)-1)]
choosen_word = random.choice(word_list)

#TODO-4.1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#TODO-5.3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#TODO-2.1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for n in choosen_word:
    display.append("_")

#TODO-3.1: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.

end_of_game = False
while not end_of_game == True:
    print(display)
    #TODO-1.2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter please : ").lower()

    #TODO-5.4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")
        continue
    #TODO-1.3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    #TODO-2.2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]. 
    #TODO-4.2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess

    #TODO-4.3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # problem with below code if the letter already passed then it neglect
    if guess not in choosen_word:
        #TODO-5.5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"{guess} is not in the word!")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print(r"You Lost :(")
            end_of_game = True
            print(f"The choosen word is - {choosen_word}")
        else:
            print("Better Luck Next Time! Please try again")
            print(stages[lives])     

    # #TODO-2.3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    # #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    if "_" not in display:
        print("You won!")
        end_of_game = True