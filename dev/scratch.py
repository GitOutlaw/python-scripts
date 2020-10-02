# User Defined Function


def add(a, b):
    sum = a + b
    return sum

def subtract(a, b):
    sum = a - b
    return sum

def multiply(a, b):
    sum = a - b
    return sum

def divide(a, b):
    sum = a - b
    return sum




# Program

one = int(input("Enter First Number: "))
two = int(input("Enter Second Number: "))

result = add(one, two)
print(f"{one} + {two} = {result}")

one = int(input("Enter First Number: "))
two = int(input("Enter Second Number: "))

result = subtract(one, two)
print(f"{one} - {two} = {result}")

one = int(input("Enter First Number: "))
two = int(input("Enter Second Number: "))

result = multiply(one, two)
print(f"{one} - {two} = {result}")            