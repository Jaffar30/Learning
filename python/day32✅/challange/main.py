import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

my_email = "ahmedmh2209@gmail.com"
password = "password :)"

if weekday == 0:
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email , msg=f"Subject:Sunday Motivation \n\n {quote}")
