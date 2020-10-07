while True:
    age = input("Please enter your age: ")
    
    if not type(age) is int:
        raise TypeError("Only INTEGERS are allowed")
    else:
        print(f'You are {age} years old')
        