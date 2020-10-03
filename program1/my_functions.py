import calendar
import string
import secrets


def user_info():
    user_name = input('Enter your name: ')
    user_age = input('Enter your age: ')
    print(f'Welcome {user_name}, you are {user_age}')

  
def calculation():
    num_1 = int(input('Enter a number: '))
    num_2 = int(input('Enter another number: '))
    total = num_1 * num_2
    print(f'{num_1} times {num_2} equals {total}')
    if total >= 100:
        print('Thats a big number!')
    else:
        print('That\'s not a big number')


def my_calender():
    
    rsp = input('Would you like to see the 2020 calender: Y/N ')
    if rsp == 'y':
        print('Here is the 2020 year calender')
        print(calendar.calendar(2020))
    if rsp == 'n':
        pass


def password_generator():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    print(password)




    
