import string
import secrets


def password_generator():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    print(password)
    
    
