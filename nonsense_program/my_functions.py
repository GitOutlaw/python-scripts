import calendar
import string
import secrets


def user_info():
    user_name = input('Enter your name: ')
    user_age = int(input('Enter your age: '))
    year = 2020 - user_age + 100
    print(f'Welcome {user_name}, you are {user_age}. You will be 100 in the year {year}')


def calculation():
    while True:
        try:
            num_1 = int(input("Enter a number to multiply: "))
            num_2 = int(input("Enter another number to multiply: "))
            total = num_1 * num_2
        except ValueError:
            print("Sorry, I didn't understand that, starting over")            
            continue
        else:            
            print("Multiply")
            print(f'{num_1} x {num_2} = {total}')
        if input('Do You Want To Multiply more numbers? y/n ') != 'y':
            break
            

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
    print(f'Random Password Generated: {password}')
    
    
def payroll():
    hourly_rate = float(input('Enter your hourly pay: '))
    hours_worked = float(input('Enter your hours worked'))
    gross_pay = hourly_rate * hours_worked
    print(f'Your gross pay is {gross_pay:.2f}')
