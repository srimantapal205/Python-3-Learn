'''
Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes to organize and structure code. It enables encapsulation, inheritance, and polymorphism, making programs modular, flexible, and easier to maintain. Here's a breakdown of the key concepts:

Class: A class is a blueprint for creating objects. It defines the structure and behavior (methods) of the objects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

Object: An object is an instance of a class. It represents a real-world entity with properties (attributes) and actions (methods).

person1 = Person("Alice", 25)
print(person1.name)  # Alice


Encapsulation: Encapsulation restricts direct access to certain attributes or methods, providing controlled access using getters and setters. Use underscores for private attributes.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500


Inheritance: Inheritance allows one class (child) to inherit attributes and methods from another class (parent). It promotes code reuse.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()  # Dog barks

Polymorphism: Polymorphism allows methods to have different implementations depending on the object or context.

class Bird:
    def sound(self):
        print("Chirp")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Bird())  # Chirp
make_sound(Cat())   # Meow

Abstraction: Abstraction hides implementation details and shows only essential features. In Python, it can be achieved using abstract base classes (ABCs).


Method Overriding: Child classes can provide specific implementations of methods from their parent class.
class Vehicle:
    def fuel(self):
        print("Uses fuel")

class ElectricCar(Vehicle):
    def fuel(self):
        print("Uses electricity")

car = ElectricCar()
car.fuel()  # Uses electricity



'''
class BigObject: # Class
    # Code
    pass

obj1 = BigObject() # Instanciate 



print(type(None)) # <class 'NoneType'>
print(type(True)) # <class 'bool'>
print(type(5))    # <class 'int'>
print(type(5.5))  # <class 'float'>
print(type('hi')) # <class 'str'>
print(type([]))   # <class 'list'>
print(type({}))   # <class 'dict'>
print(type(()))   # <class 'tuple'>

# Define the PlayerCharacter class
class PlayerCharacters : 
    def __init__(self, name, age):
        # Assign the name and age to the object
        self.name = name #attribute
        self.age = age #attribute
        
    # Method for the character to perform an action
    def run(self):
        print('Run')
        return 'done'
# Create player objects
player1 = PlayerCharacters('Cindy', 24)
player2 = PlayerCharacters('Tom', 21)
print(player1.run())
print(player2.name)

help(list)

