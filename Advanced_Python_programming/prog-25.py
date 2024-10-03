#Explain Inheritance in Python with an example? What is init? Or What Is A Constructor In Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal): 
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Buddy")

print(dog.speak())  


# Inheritance allows a class to inherit properties and methods from another class. 
# It is a way to reuse code across multiple classes.

# Base Class (Parent/Superclass): The class whose properties and methods are inherited.
# Derived Class (Child/Subclass): The class that inherits the properties and methods of the base class.


# __init__ (Constructor):
# The __init__ method is called a constructor. It is automatically invoked when an object is instantiated (created) from a class.
# It is used to initialize the instance attributes (variables) of the class.