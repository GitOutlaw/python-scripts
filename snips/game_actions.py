import random

# character roles


class Warrior:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack_cleave(self):
        min_value = 55
        max_value = 100
        print(
            f'{self.name} uses {self.power} for an attack of {random.randint(min_value, max_value)} .')

    def attack_rend(self):
        min_value = 35
        max_value = 100
        print(f'{self.name} uses {self.power} for an attack of <{random.randint(min_value, max_value)}> .')


class Wizard:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack_lighting(self):
        min_value = 47
        max_value = 100
        print(f'{self.name} uses {self.power} for an attack of <{random.randint(min_value, max_value)}> .')

    def attack_fire_ball(self):
        min_value = 47
        max_value = 100
        print(f'{self.name} uses {self.power} for an attack of <{random.randint(min_value, max_value)}> .')

    def heal(self):
        pass


class Ranger:

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack_pierce(self):
        min_value = 60
        max_value = 100
        # print(random.randint(min_value, max_value))
        print(f'{self.name} uses {self.power} for an attack of <{random.randint(min_value, max_value)}>.')

    def attack_long_shot(self):
        min_value = 45
        max_value = 100
        # print(random.randint(min_value, max_value))
        print(f'{self.name} uses {self.power} for an attack of <{random.randint(min_value, max_value)}>.')

    def heal(self):
        pass


ranger1 = Ranger('Max', 'Pierce')
wizard1 = Wizard('Merlin', 'Lighting')
warrior1 = Warrior('Conan', 'Rend')


ranger1.attack_pierce()
wizard1.attack_fire_ball()
warrior1.attack_rend()
