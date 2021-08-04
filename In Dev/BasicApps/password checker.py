# Import module getpass
import getpass

# ---- Global Variables ----

def check_password():
    user_name = input('What is your username?: ')
    user_password = getpass.getpass('Please enter your password: ')
    password_length = len(user_password)
    hidden_password = '*' * password_length
    print(f'{user_name} your {hidden_password} is {password_length} characters long')


check_password()