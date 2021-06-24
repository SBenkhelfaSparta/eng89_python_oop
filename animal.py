class Animal:

    def __init__(self): # we decalre attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive!"

    def eat(self):
        return "time to eat"

    def move(self):
        return "Move left and right to stay awake"

# we need to create an object of this class in order to use any methods
#cat = Animal() #creating an object of Animal Class
#print(cat.eat())