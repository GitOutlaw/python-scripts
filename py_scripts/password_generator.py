import string
import secrets


def password_generator(): 
        print('Password Generator')
        try:
            characters = int(input('How many characters to: '))

        except ValueError:
            print("Please enter a number")            
            # continue
        else:
            alphabet = string.ascii_letters + string.digits
            password = ''.join(secrets.choice(alphabet) for i in range(characters))
            print(password)
           
            
password_generator()  
