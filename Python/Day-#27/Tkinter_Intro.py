# Pirates of silicon valley - to know background about silicon valley

# Wrapper functions for Tcl/Tk.

# Tkinter provides classes which allow the display, positioning and control of widgets. Toplevel widgets are Tk and Toplevel. Other widgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton, Checkbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox LabelFrame and PanedWindow.

# Properties of the widgets are specified with keyword arguments. Keyword arguments have the same name as the corresponding resource under Tk.

# Widgets are positioned with one of the geometry managers Place, Pack or Grid. These managers can be called with methods place, pack, grid available in every Widget.

# Actions are bound to events by resources (e.g. keyword argument command) or with the method bind.

# Example (Hello, World): 
# import tkinter 
# from tkinter.constants import * 
# tk = tkinter.Tk() 
# frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2) 
# frame.pack(fill=BOTH,expand=1) 
# label = tkinter.Label(frame, text="Hello, World") 
# label.pack(fill=X, expand=1) 
# button = tkinter.Button(frame,text="Exit",command=tk.destroy) 
# button.pack(side=BOTTOM) 
# tk.mainloop()

import tkinter
from typing import Text

window = tkinter.Tk()
window.title("Tkinter's First GUI")
window.minsize(width=500, height=300)

#Labels 
my_lable = tkinter.Label(text="This is a Label", font=("Fira Code", 14, "bold"))
my_lable.pack() # default is center
# my_lable.pack(side="left")

# 3 ways of configuring the labels
# my_lable = tkinter.Label()
# my_lable["text"] = "lable text"
# my_lable.config(text="New_text")
# my_lable.pack(side="left")

# Entry
input = tkinter.Entry()
input.config(width=10)
input.pack()

def button_clicked():
    # my_lable.config(text="Button Got Clicked")
    input.get()
    my_lable.config(text=f"Hi There! - {input.get()}")
    my_lable.pack()

# Button
button = tkinter.Button(text="Click Me", font=("Fira Code", 10, "bold"), command=button_clicked)
button.pack()


# Scale, SpinBox, Checkbox, ListBox, RadioButton

window.mainloop()