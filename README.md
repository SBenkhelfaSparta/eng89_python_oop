# Python Object-Oriented Programming
## Four Pillars of OOP
### Functions and good practice of functions
#### DRY - Don't Repeat Yourself
- Syntax:   def function_name(parameter1, parameter2):

```python
# First Iteration
def greeting():
    print("Welcome on board! Enjoy your trip.")
# pass allows the interpreter to escape the function without errors

greeting()  # You need to call the function for it to execute
```
```python
# Second iteration using RETURN statement
def greeting():
    print("Good morning")
    return "Welcome on board! Enjoy your trip."

print(greeting())
```
```python
# Third iteration with user name as a string as an argument
def greeting(name):
#    print(name)
    return "Welcome on board " + name

print(greeting("James"))  # We need to pass an argument for the name parameter
```
```python
# Create a function to prompt the user to enter their name and display the name back to the user with greeting message
def greetings(name):
    return "Welcome " + name

user_name = input("Please tell me your name:  ")
print(greetings(user_name))
```
```python
# Create a function with multiple args as an int
def add(num1, num2):
    return num1 + num2

print(add(9, 3))

def multiply(num1, num2):
    return num1 * num2
    # Any code after return (that is inside the function) will not execute

print(multiply(2, 3))
```