# How to send email

# import smtplib
# import os
# from dotenv import load_dotenv
#
# load_dotenv("/Users/Ryuuuu/PycharmProjects/Send_Email/.env")
#
# MY_EMAIL = os.getenv("MY_EMAIL")
# MY_PASSWORD = os.getenv("MY_PASSWORD")
#
# with smtplib.SMTP("smtp.gmail.com", 587)  as connection:
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=MY_EMAIL,
#         msg="Hello!!"
#     )


from datetime import datetime
import pandas
import random
import smtplib

import os
from dotenv import load_dotenv

load_dotenv("/Users/Ryuuuu/PycharmProjects/Send_Email/.env")

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
