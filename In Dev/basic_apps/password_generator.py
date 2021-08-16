import string
import secrets


def password_generator():
    while True:
        try:
            characters = int(input('How many characters: '))
        except ValueError:
            print("Please enter a number and try again")
            continue           
        else:
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet) for i in range(characters))
            print(password)
            break         
                       
password_generator()  