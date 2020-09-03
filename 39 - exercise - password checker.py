# Import module getpass
import getpass

# ---- Global Variables ----

# User input user name
user_name = input('What is your username?: ')

# User inputs password and is not displayed on the screen
user_password = getpass.getpass('Please enter your password: ')

# Password length function
password_length = len(user_password)

# Changes password_length to diplay '*' hidding the users password  
hidden_password = '*' * password_length

# Prints results to user
print(f'{user_name} your {hidden_password} is {password_length} characters long')