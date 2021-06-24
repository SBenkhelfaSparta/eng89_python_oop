from animal import Animal #importing Animal class

class Reptile(Animal): #inherits form Animal class

    def __init__(self):
        super().__init__() #super is used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "it's chilly, looking to have fun in the sun!"

    def hunt(self):
        return "keep working hard to find food"

    def use_venom(self):
        return "If I have it I will use it"

rep = Reptile()
print(rep.breathe())
print(rep.hunt())
print(rep.eat())
print(rep.move())
