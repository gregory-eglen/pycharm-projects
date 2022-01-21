# NameAge.py
# Created by: Gregory Eglen
# A program that takes inputs for a users name, the month and day they were born, and their age and calculates
# the year the user was born

from datetime import datetime

# Gets user name and checks that at least one character was entered
name = input('What is your name?\n')

while len(name) == 0:
    print('You must have a name.')
    name = input('What is your name?\n')

# Gets month user was born and checks that it would be valid (1-12)
birthday_month = int(input('Enter the month of your birthday as a number (e.g. August = 8)\n'))

while birthday_month <= 0 or birthday_month >= 13:
    print('Please enter a valid birthday month (1-12)\n')
    birthday_month = int(input('Enter the month of your birthday as a number(e.g. August = 8)\n'))

# Gets day of the month user was born and checks for validity (1-31)
birthday_day = int(input('Enter the day of the month you were born.\n'))

while birthday_day < 1 or birthday_day >= 32:
    print('Please enter a valid day of the month (1-31)\n')
    birthday_day = int(input('Enter the day of the month you were born.\n'))

# Gets age of the user and makes sure the number is not negative
age = int(input('How old are you?\n'))

while age < 0:
    print('You can not be negative years old.\n')
    age = int(input('How old are you?\n'))

# Sets variables for today's date
now = datetime.now()
year = int(now.strftime('%Y'))
month = int(now.strftime('%m'))
day = int(now.strftime('%d'))

# Program output
if birthday_month < month:
    print('Hello', name + '!', 'You were born in', str(year - age) + '.')
elif birthday_month == month:
    if birthday_day <= day:
        print('Hello', name + '!', 'You were born in', str(year - age) + '.')
    else:
        print('Hello', name + '!', 'You were born in', str(year - age - 1) + '.')
else:
    print('Hello', name + '!', 'You were born in', str(year - age - 1) + '.')
