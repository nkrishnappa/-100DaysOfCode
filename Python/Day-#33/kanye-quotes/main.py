from tkinter import *
import requests

BACKGROUND_IMAGE = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#33\kanye-quotes\background.png"
KANYE_PNG = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#33\kanye-quotes\kanye.png"

KANYE_API_ENDPOINT = r"https://api.kanye.rest/"
# {
#   "quote": "There's a crying need for civility across the board. We need to and will come together in the name of Jesus."
# }

def get_quote():
    response = requests.get(url=KANYE_API_ENDPOINT)
    response.raise_for_status()
    json_data = response.json()
    canvas.itemconfig(quote_text, text=json_data["quote"])

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=BACKGROUND_IMAGE)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Fira Code", 15, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=KANYE_PNG)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()