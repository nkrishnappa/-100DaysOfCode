import pandas 
import datetime
import random
import smtplib

letters_path = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#32\letter_templates"
LETTERS = [f"{letters_path}/letter_1.txt", f"{letters_path}/letter_2.txt", f"{letters_path}/letter_3.txt"]

my_email = "nandishakrishnappa186@gmail.com"
password = "Nandish@123"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

birthday_csv = r"C:\Users\nkrishnappa\Desktop\100DaysOfCode\Python\Day-#32\birthdays.csv"
birthday_dataframe = pandas.read_csv(birthday_csv)

# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
today_birthday_dataframe = birthday_dataframe[(birthday_dataframe.day == now.day) & (birthday_dataframe.month == now.month)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
count = len(today_birthday_dataframe)
print(f"found {count} birthday[s] today - {now.day}/{now.month}/{now.year}")
if count:
    for indices, row in today_birthday_dataframe.iterrows():
        birthday_boy_girl = row['name']
        receiver_email = row['email']

        letter = random.choice(LETTERS)
        with open(letter, "r") as file:
            letter_content = file.read().replace("[NAME]", birthday_boy_girl)

        # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiver_email,
                                msg=f"Subject:Happy BirthDay {birthday_boy_girl}\n\n {letter_content}"
                )