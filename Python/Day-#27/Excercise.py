import tkinter

window = tkinter.Tk()
window.title("Tkinter GUI")
window.minsize(width=400, height=300)
window.config(padx=50, pady=50)

# Entry
input = tkinter.Entry()
input.config(width=10, font=("Fira Code", 10, "bold"))
input.grid(column=4, row=3)

#Labels 
my_lable = tkinter.Label(text="Label", font=("Fira Code", 14, "bold"))
my_lable.config(padx=20, pady=20)
my_lable.grid(column=1, row=1)

def button_clicked():
    # my_lable.config(text="Button Got Clicked")
    input.get()
    my_lable.config(text=f"Hi There! - {input.get()}")

# Button
button = tkinter.Button(text="Click Me", font=("Fira Code", 10, "bold"), command=button_clicked)
button.config(padx=20, pady=20)
button.grid(column=2, row=2)

def button_clicked_new():
    print("2nd button clicked")

nw_button = tkinter.Button(text="New Button!", font=("Fira Code", 10, "bold"),  command=button_clicked_new)
nw_button.config(padx=20, pady=20)
nw_button.grid(column=3, row=1)

window.mainloop()