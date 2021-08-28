from tkinter import *

import math

image_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#28\tomato.png"
FONT = ("Fira Code", 25, "bold")

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer_coundown_call = None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_coundown_call)
    global reps
    reps = 0

    canvas.itemconfig(timer_text, text="00:00", font=FONT)
    timer_label.config(text="Timer", font=FONT, fg=GREEN)
    check_box.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
# Start Button
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    reps += 1 
    if reps % 2 == 1:
        timer = work_sec
        timer_label.config(text="Work", font=FONT, fg=GREEN)
    elif reps % 8 == 0:
        timer = long_break
        timer_label.config(text="Break", font=FONT, fg=RED)
    else:
        timer = short_break
        timer_label.config(text="Break", font=FONT, fg=PINK)

    countdown(timer)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count_time):
    format_time_min = math.floor(count_time / 60)
    format_time_sec = count_time % 60
    canvas.itemconfig(timer_text, text=f"{format_time_min:02d}:{format_time_sec:02d}")
    # canvas.create_text(100, 112, text=f"{count_time}", fill="white", font=FONT)
    if count_time > 0:
        global timer_coundown_call
        timer_coundown_call = window.after(1000, countdown, count_time -1)
    else:
        start_timer()
        ticks = "✔" * int(reps / 2) 
        check_box.config(text=ticks)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50, bg=YELLOW)
window.title("Pomodora") # Tomoto in italian

# Canvas Widget
canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
pomodora_img = PhotoImage(file=image_path)
canvas.create_image(100, 112, image=pomodora_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=FONT)
canvas.grid(column=2, row=2)

# label
timer_label = Label(text="Timer", font=("Fira Code", 25, "normal"), fg=GREEN)
timer_label.config(padx=20, pady=10, bg=YELLOW)
timer_label.grid(column=2,row=1)

start_button = Button(text="Start", command=start_timer, font=("Fira Code", 10, "normal"))
start_button.config(padx=5, pady=5, bg=YELLOW)
start_button.grid(column=1, row=3)

# Reset Button
reset_button = Button(text="Reset", command=reset_timer, font=("Fira Code", 10, "normal"), anchor="n")
reset_button.config(padx=5, pady=5, bg=YELLOW)
reset_button.grid(column=3, row=3)

# CheckMark
check_box = Label(fg=GREEN, bg=YELLOW)
check_box.grid(column=2, row=4)

window.mainloop()