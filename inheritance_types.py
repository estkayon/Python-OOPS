# # Single or Basic Inheritance

# # Base class
# class Parent:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

# # Derived class
# class Child(Parent):

#     def play(self):
#         print(f"{self.name} is playing.")

# # Create an instance of Child
# child = Child("Alice")
# child.greet()  # Output: Hello, my name is Alice.
# child.play()   # Output: Alice is playing.

# ------------------------------------------------------------

# Multilevel Inheritance

# Base class
class Grandparent:
    def __init__(self, name):
        self.name = name

    def tell_story(self):
        print(f"{self.name} tells a story.")

# Intermediate class
class Parent(Grandparent):

    def work(self):
        print(f"{self.name} is working.")

# Derived class
class Child(Parent):

    def play(self):
        print(f"{self.name} is playing.")

# Create an instance of Child
child = Child("Charlie")
child.tell_story()  # Output: Charlie tells a story.
child.work()        # Output: Charlie is working.
child.play()        # Output: Charlie is playing.

# -----------------------------------------------------------