class Whale:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def eat(self):
            print(f'{self.name} is eating')

    def sleep(self):
            print(f'{self.name} is sleeping')

class SeiWhale(Whale):
    pass

class BlueWhale(Whale):
    pass

seiWhale = SeiWhale('Sey')
blueWhale = BlueWhale('Blo')

print(blueWhale.name)
print(blueWhale.is_alive)
blueWhale.eat()