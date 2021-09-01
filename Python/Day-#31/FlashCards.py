from tkinter import * 
from tkinter import messagebox
import pandas
from random import choice
import time

BACKGROUND_COLOR = "#B1DDC6"
RIGHT = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\images\right.png"
WRONG = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\images\wrong.png"
CARD_FRONT = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\images\card_front.png"
CARD_BACK = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\images\card_back.png"
CSV_FILE = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\data\french_words.csv"
WORDS_TO_LEARN = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#31\data\words_to_learn.csv"

try:
    data = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    data = pandas.read_csv(CSV_FILE)
finally:
    # orient - records - List of dictionary , each row as list
    learn_word = data.to_dict(orient="records") 

random_word = {}

def display_next():
    global random_word, flip_timer
    window.after_cancel(flip_timer)

    random_word = choice(learn_word)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word['French'], fill="black")
    canvas.itemconfig(canvas_image, image=canvas_photoimage)
    flip_timer = window.after(3000, func=flipcard)
    
def known_function():
    learn_word.remove(random_word)
    # learn_word.remove({'French': 'partie', 'English': 'part'})

    dataframe = pandas.DataFrame(learn_word)
    dataframe.to_csv(WORDS_TO_LEARN,index=False)
    display_next()

def flipcard():
    canvas.itemconfig(canvas_image, image=canvas_new_photoimage)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word['English'], fill="white")
    

window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flipcard)

canvas = Canvas(width=800, height=526)
canvas_photoimage = PhotoImage(file=CARD_FRONT)
canvas_image = canvas.create_image(400, 263, image=canvas_photoimage)
canvas_new_photoimage = PhotoImage(file=CARD_BACK)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = canvas.create_text(400, 150, font=("Fira Code", 30, "italic"))
word_text = canvas.create_text(400, 263, font=("Fira Code", 40, "bold"))
canvas.grid(column=1, row=1, columnspan=2)

wrong_image = PhotoImage(file=WRONG)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=display_next)
wrong_button.grid(column=1,row=2)

right_image = PhotoImage(file=RIGHT)
right_button = Button(image=right_image, highlightthickness=0, command=known_function)
right_button.grid(column=2,row=2)
display_next()

window.mainloop()