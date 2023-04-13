import string
import secrets


website = input("Enter website: ")
user_name = input("Enter your username: ")


def password_generator():
    while True:
        try:
            characters = int(input('How many characters: '))
        except ValueError:
            print("Please enter a number and try again.")
            continue
        else:
            alphabet = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(secrets.choice(alphabet)
                               for i in range(characters))
            print(f"Domain: {website}")
            print(f"Username: {user_name}")
            print(f"Password: {password}")
            break


password_generator()
