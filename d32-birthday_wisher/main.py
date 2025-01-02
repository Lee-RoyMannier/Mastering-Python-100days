import smtplib
from random import randint, choice
import pandas as pd
from datetime import datetime

EMAIl = MAIL
PASSWORD = PASSWORD

date = datetime.today()
actual_date = (date.month, date.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(row.month, row.day): row for index, row in data.iterrows()}
birthdays_date = birthdays_dict.keys()
for birthday in birthdays_date:
    if actual_date == birthday:
        letters = choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])

        try:
            with open(f"letter_templates/{letters}", "r") as f:
                letter = f.read()
        except FileNotFoundError:
            print("letter file not found")
        else:
            letter = letter.replace("[NAME]", birthdays_dict[birthday]["name"])
        finally:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIl, PASSWORD)
                smtp.sendmail(
                    to_addrs=birthdays_dict[birthday]["email"],
                    from_addr=EMAIl,
                    msg=f"Subject: Birthday wisher!\n\n{letter}")



