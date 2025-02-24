#import smtplib

MY_EMAIL = "hailesbales1244@gmail.com"
MY_PASSWORD = "ykanesagnzvjfonj"
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls() # transport layer security designed to provide communications security over a computer network
#    connection.login(user=my_email, password=my_password)
#
#    connection.sendmail(
#        from_addr=my_email,
#        to_addrs="hailesbales1234@yahoo.com",
#        msg="Subject:Email Test\n\nThis is verfied test from pycharm"
#    )


# current date and time
#current = dt.datetime.now()
#year = current.year
#month = current.month
#days_of_week = current.weekday()


#date_of_birth = dt.datetime(year= 1997, month= 11, day= 25)
#print(date_of_birth)

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}")