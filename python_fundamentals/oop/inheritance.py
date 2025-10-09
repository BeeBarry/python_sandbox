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
    def __init__(self,name): # I need to declare these arguments so they can be recevied when constructing.
        super().__init__(name)

    def longtravel(self):
        print(f'{self.name} is commencing a long distance travel..')

seiWhale = SeiWhale('Sey')
blueWhale = BlueWhale('Blo')

print(blueWhale.name)
print(blueWhale.is_alive)
blueWhale.eat()

print(seiWhale.name)
print(seiWhale.is_alive)

blueWhale.longtravel()