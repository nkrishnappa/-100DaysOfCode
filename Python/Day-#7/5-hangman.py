import random
from hangman_words import word_list
from hangman_logo import stages, logo 

choosen_word = random.choice(word_list)
lives = 6
print(logo)

display = []
for n in choosen_word:
    display.append("_")

end_of_game = False
while not end_of_game == True:

    guess = input("Guess a letter please : ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
        continue

    for position in range(len(choosen_word)):
        if choosen_word[position] == guess:
            display[position] = guess
    print(f"{' '.join(display)}")

    if guess not in choosen_word:
        print(f"{guess} is not in the word.. you lose a life..")
        lives -= 1
        if lives == 0:
            print(stages[lives])
            print(r"You Lost :(")
            end_of_game = True
            print(f"The choosen word is - {choosen_word}")
        else:
            print(stages[lives])     

    if "_" not in display:
        print("You won!")
        end_of_game = True