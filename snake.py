# ### Snake class

# #### Create a Snake class

from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


    def use_tongue_to_smell(self): # Adding some specific methods/behaviours
        return " *Hiss* "

#
# smart_snake = Snake()
# print(smart_snake.move()) # move() is available from Animal class
# print(smart_snake.hunt())# hunt () is available from Reptile class