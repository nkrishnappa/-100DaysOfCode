# 1. pack
# 2. Place
# 3. Grid

from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=200, height=200)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
# label.place(x=100, y=50)
label.grid(column=0, row=0)

# Button
def button_click():
    print("Button pressed")
button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=3)

window.mainloop()
