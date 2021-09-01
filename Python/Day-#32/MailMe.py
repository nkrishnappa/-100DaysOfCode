# smtp.gmail.com - Gmail

import smtplib
import datetime
import random

motivation_file = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#32\quotes.txt"
my_email = "nandishakrishnappa186@gmail.com"
password = "Nandish@123"

now = datetime.datetime.now()
if now.weekday() == 2:
    with open(motivation_file, "r") as file:
        quote_bank = file.read().split("\n")

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()
        quote_of_the_day = random.choice(quote_bank)
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="www.nandishraina@gmail.com",
                            msg=f"Subject:Monday Motivation\n\n {quote_of_the_day}"
            )
        # connection.close()
