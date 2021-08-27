from tkinter import *

FONT = ("Fira Code", 10, "normal")

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
window.minsize(width=400, height=100)

# Entry
input = Entry()
input.config(width=20)
input.grid(column=2, row=1)

# Label
is_equal_label = Label(text="is equal to", font=FONT)
is_equal_label.config(padx=20, pady=20)
is_equal_label.grid(column=1, row=2)

miles_label = Label(text="Miles", font=FONT)
miles_label.config(padx=20, pady=20)
miles_label.grid(column=3, row=1)

km_label = Label(text="Km", font=FONT)
km_label.config(padx=20, pady=20)
km_label.grid(column=3, row=2)

result_label = Label(text="0", font=FONT)
result_label.config(padx=20, pady=20)
result_label.grid(column=2, row=2)

def convert_to_km():
    miles = input.get()
    km = round(float(miles) * 1.609344, 2)
    result_label.config(text=f"{km}")

# button
calculate_button = Button(text="Calculate", command=convert_to_km)
calculate_button.config(padx=20, pady=20)
calculate_button.grid(column=2, row=3)

window.mainloop()

