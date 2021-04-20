

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat('Butters', 12)
cat2 = Cat('Kitty', 8)
cat3 = Cat('Misty', 9)
cat4 = Cat('Whiskers', 15)

def find_oldest_cat(*args):
    return max(args)


print(f'The oldest cat is {find_oldest_cat(cat1.age, cat2.age, cat3.age, cat4.age)}')