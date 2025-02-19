import smtplib

my_email = "hailesbales1244@gmail.com"
my_password = "ykanesagnzvjfonj"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # transport layer security designed to provide communications security over a computer network
    connection.login(user=my_email, password=my_password)

    connection.sendmail(
        from_addr=my_email,
        to_addrs="hailesbales1234@yahoo.com",
        msg="Subject:Email Test\n\nThis is verfied test from pycharm"
    )