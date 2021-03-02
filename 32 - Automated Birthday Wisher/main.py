import smtplib
import datetime
import pandas
import random

EMAIL = "email@server.com"
PASSWORD = "1234PASS"

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrrows()}

if today in birthdays_dict:
    birthday_match = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_match["name"])

    with smtplib.SMTP("smtp.server.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_match["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )