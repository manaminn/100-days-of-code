# import smtplib
#
# my_email = "manamihikita14@gmail.com"
# password = "uqwqdhgveivwcgtx"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="manamihikita871@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
#
#
# date_of_birth = dt.datetime(year=2007, month=3, day=7)
# print(date_of_birth)
import random
import smtplib
import datetime as dt

now = dt.datetime.now()
day = now.weekday()
my_email = "manamihikita14@gmail.com"
password = "uqwqdhgveivwcgtx"

if day == 4:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    chosen_quote = random.choice(quotes)
    print(chosen_quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mikako.hikita@gmail.com",
            msg=f"Subject:Monday motivational quotes\n\n{chosen_quote}"
        )


