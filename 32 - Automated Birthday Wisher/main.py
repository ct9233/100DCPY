import smtplib
import datetime
import pandas

EMAIL = "email@server.com"
PASSWORD = "1234PASS"

now = datetime.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")



with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(EMAIL, PASSWORD)