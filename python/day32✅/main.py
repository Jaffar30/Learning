from datetime import datetime
import pandas
from random import randint
import smtplib

my_email = "ahmedmh2209@gmail.com"
password = "password :)"

today = (datetime.now().month,datetime.now().day)

data = pandas.read_csv("birthdays.csv")

bd_dict = {(data_row['month'] , data_row['day']) : data_row for (index,data_row) in data.iterrows()}

if today in bd_dict:
    receiver_info = bd_dict[today]
    file = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file) as letter:
        content = letter.read()
        content = content.replace("[NAME]", receiver_info['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=receiver_info['email'] , msg=f"Subject:Happy Birthday \n\n {content}")
