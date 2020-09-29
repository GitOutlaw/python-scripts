import datetime



def border():
    print('-' * 63)

border()

def sys_info():
    
    print('Welcome to Adam\'s Grocery Store Pay Calculator version: 0.0.1')
    today = datetime.datetime.today()
    date = today.strftime('%m/%d/%Y')
    time = today.strftime('%H:%M:%S')
    print(f'| System Date: {date} | System Time: {time} |')
    
sys_info()

border()


def operation():
    employee_name = (input('Enter your Name: '))
    hours = float(input('How many hours have you worked: '))
    rate = float(input('What is your hourly rate: '))
    pay = hours * rate
    print()

    if hours <= 40:
        print(f'{employee_name}, your gross pay is: ${pay}0')

    else:
        pay = (40 * rate) + (hours - 40) * (1.5 * rate)
        print(f'{employee_name}, your gross pay with overtime is: ${pay}0')


operation()

print()
border()
print('<---> End Program <--->')

