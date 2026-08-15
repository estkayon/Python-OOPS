# Single or Basic Inheritance

# Base class
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Derived class
class Child(Parent):

    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Alice")
child.greet()  # Output: Hello, my name is Alice.
child.play()   # Output: Alice is playing.

