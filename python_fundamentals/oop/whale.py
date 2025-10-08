class Whale:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def sing(self):
        print(f'{self.name} is now singing a jazzy tune')

    def sleep(self):
        print(f'{self.name} is now entering a coozy dream...')

    def wakeup(self):
        print(f'{self.name} is now slowly waking up...')

    def birthday(self):
        print(f'{self.name} is now celebrating its {self.age} year birthday')