import random
import datetime
import smtplib

DAYS_OF_WEEK = {
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6,
}
SMTP_SERVER_ADDRESS = 'type server address here'
TEST_EMAIL = 'type sender email here'
TEST_EMAIL_PASSWORD = 'type sender password here'
RECEIVER_EMAIL = 'type receiver email here'

with open(file='./quotes.txt', mode='r') as file:
    quotes_list = file.readlines()
    random_index = random.choice(seq=quotes_list)
    random_quote = '"' + quotes_list[quotes_list.index(random_index)].strip().split(sep='"')[1] + '"'
    corresponding_author = quotes_list[quotes_list.index(random_index)].strip().split(sep='"')[2]

if datetime.datetime.now().weekday() == DAYS_OF_WEEK['Monday']:
    with smtplib.SMTP(host=SMTP_SERVER_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL, password=TEST_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=TEST_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg='Subject:Some Monday Inspiration\n\n'
                f'{random_quote}{corresponding_author}'
        )
