# Python OOP
## Four Pillars of OOP
### Functions and good practice of functions
```python
# creating a function
# syntax def name_of_function(inputs) is used to declare a function

def greeting():
    print("Welcome on board, enjoy your trip!")
# pass can be used to skip without any errors

greeting() # function must be called to give output
```
- calling the above function will print out the string as the print statement is part of the function
- functions can also have a return function which returns variables which can later be called:
```python
def greeting():
    print("Good morning.")
    return "Welcome on board, enjoy your trip!"

print(greeting())
```
- this function will print the `"Good morning."` string then print the returned string afterwards
- the returned line is always what is outputted last from the function
- functions can take inputs from either the code or user inputs and run the code with this data:
```python
def greeting(name):
    return "Welcome on board " + name + "!"

print(greeting("Tom")) # this line is calling the function for "Tom"
```
```python
def greeting(name):
    return "Welcome on board " + name + "!"

print(greeting(input("What is your name?  ").capitalize()))
```
- functions can take multiple arguments
```python
def add(num1, num2):
    return num1 + num2

print(add(2, 3))
```
- this will return `5`
```python
def multiply(num1, num2):
    return num1 * num2
    print("this is the required outcome of two numbers") # this line will not execute as it is after return statement
    
print(multiply(3, 5))
```
- this will only return `15`, any required methods must come before the return statement
#### DRY Don't Repeat Yourself

### Python modules, packages and libraries
- modules contain built in functions and can be imported into a code script
- `import` is the key word used to import classes
```python
import math # imports whole class
from random import random # imports specific file from class

num1 = 23.44 # float

# have to round figure depending on value
# if value is less the .50 round down, if .50 or above round up

print(math.ceil(num1)) # rounds up to next integer
print(math.floor(num1)) # rounds down to next integer
print(math.pi)

# if specific file is imported it doesn't need to be called from class
print(random()) # random number between 0 and 1 everytime it is run
```
- imports can be used to get system and OS info, and also can be imported in groups
```python
import os # used to get information about your OS
import datetime, sys # sys is used to get system specific info

work_dir = os.getcwd() # provides current location/path
print(work_dir)
print(os.getuid()) # user id
print(os.cpu_count()) # reads hardware info - counts CPUs of machine
print(os.uname()) # returns username

print(datetime.date.today()) # today's date
print(sys.path) # absolute path
```
- requests is a package to interact with a live API - we can make an API call to any web address using python requests package
- packages must be explicitly installed if not available by default
- `pip install package_name` is the method in the console
```python
import requests # installed via pip method first
```
is done after `pip install requests`
- `pip -V` returns version
```python
requests_api = requests.get("https://www.bbc.co.uk/")
print(requests_api.status_code) # 200 for success, 404 and above for fail/unavailable
print(requests_api.headers)
print(requests_api.content)
```
- ensure URL is exact - copy and paste
- can slice up data to get specifics
- can check data types with `type(data)`
- use `if` to check status code and ensure website is live before scraping any data

- step one create an animal.py file to create parent class
- step two to create file called reptile.py to abstract data and inherit from animal.py
- step three is to create a file called snake.py
- step four is to create a file called python.py and this point we should be able to utilise inheritance from multiple classes - everything available from animal class to python

### Animal class

-  follow the correct naming convention
- We need to initialise with build it method called __init__(self)
- self refers to current class
```
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
```
- We need to create an object of this class in order to use any methods
- For cat as a user the functionality inside Animal class and the method breathe is abstracted
```
cat = Animal()
print(cat.eat())
```

### Reptile class

#### Create a Reptile class to inherit Animal class

```
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

```
- Let's create an object of Reptile class
```
smart_reptile = Reptile()

print(smart_reptile.breathe()) #breathe method is inherited from Animal class
print(smart_reptile.hunt()) # hunt() is available in Reptile class
print(smart_reptile.eat())
print(smart_reptile.move())
print(smart_reptile.hunt())
```

### Snake class

#### Create a Snake class
```
from reptile import Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True


    def use_tongue_to_smell(self): # Adding some specific methods/behaviours
        return " *Hiss* "


smart_snake = Snake()
print(smart_snake.move()) # move() is available from Animal class
print(smart_snake.hunt())# hunt () is available from Reptile class
```
### Python class

#### Create a Python class
```
from snake import Snake

class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True


    def digest_large_prey(self):
        return "I can dislocate my jaw to eat you"

    def climb(self):
        return "Can't even escape me from high in trees"

    def shed_skin(self):
        return "I'm growing out of my skin"

fast_python = Python()
print(fast_python.climb())
print(fast_python.hunt())
print(fast_python.move())
print(fast_python.use_tongue_to_smell())
print(fast_python.shed_skin())
```