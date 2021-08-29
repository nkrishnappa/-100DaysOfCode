from tkinter import *
from tkinter import messagebox
import pyperclip

image_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#29\logo.png"
FONT=("Fira Code", 10, "bold")
password_data = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#29\password.txt"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    from random import choice, randint, shuffle
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "" . join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    email = email_entry.get()
    website = website_entry.get()
    pwd = password_entry.get()

    if not email or not website or not pwd:
        messagebox.showinfo(title="oops!", message="Please make sure you haven't left any fields empty") 
        return

    is_ok = messagebox.askokcancel(title=website, message=f"""These are the details entered:
    EMAIL : {email}
    Password : {pwd}
    Is it ok to save?
    """)

    if not is_ok:
        return    

    with open(password_data, "a") as password_file:
        password_file.write(f"{website} | {email} | {pwd}\n")
    
    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50 )

# Canvas Widget
canvas = Canvas(width=200, height=200, highlightthickness=0)
my_pass_image = PhotoImage(file=image_path)
canvas.create_image(100, 100, image=my_pass_image)
canvas.grid(column=2, row=1)

website_label = Label(text="Website:", font=FONT)
website_label.grid(column=1, row=2)

website_entry = Entry(width=60, font=FONT)
website_entry.grid(column=2, row=2, columnspan=3)
website_entry.focus()

email_label = Label(text="Email/Username:", font=FONT)
email_label.grid(column=1, row=3)

email_entry = Entry(width=60, font=FONT)
email_entry.grid(column=2, row=3, columnspan=3)
# email_entry.insert(END, "email.com")
email_entry.insert(0, "nandisha.krishnappa.3@email.com")

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=1, row=4)

password_entry = Entry(width=44, font=FONT)
password_entry.grid(column=2, row=4)

add_button = Button(text="Add", width=60, font=FONT, command=save_password)
add_button.grid(column=2, row=5, columnspan=3)

genpwd_button = Button(text="Generate Password", font=("Fira Code", 8, "bold"), command=password_generator)
genpwd_button.grid(column=3, row=4)




window.mainloop()

