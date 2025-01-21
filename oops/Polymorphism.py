'''
Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects of different classes to be treated as objects of a common super class. It facilitates flexibility and extensibility in a program by enabling one interface to be used for different underlying data types.

In Python, polymorphism allows different classes to define methods with the same name, but potentially different behaviors. The exact method that gets invoked depends on the type of object calling the method. This makes it possible to design systems where objects can be used interchangeably as long as they follow the expected interface.

Types of Polymorphism
Compile-Time Polymorphism (Static Polymorphism):

Achieved through method overloading (not natively supported in Python).
Multiple methods in the same class can have the same name but differ in parameters (number or type).

class MathOperations:
    def add(self, a, b, c=0):  # Optional parameter allows overloading
        return a + b + c

math_op = MathOperations()
print(math_op.add(5, 10))     # Two arguments
print(math_op.add(5, 10, 15))  # Three arguments

Run-Time Polymorphism (Dynamic Polymorphism):

Achieved through method overriding.
A subclass provides a specific implementation of a method that is already defined in its parent class.

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow

'''
#Examples of Polymorphism
#Polymorphism with Functions and Objects: Functions can take arguments of different types and still operate on them.
def add(x, y):
    return x + y

print(add(3, 5))        # Integers: 8
print(add("Hello, ", "World!"))  # Strings: Hello, World!

# Polymorphism with Classes: Objects from different classes can be used in the same context if they implement a common method.
class Bird:
    def fly(self):
        return "Flying at a moderate height."

class Airplane:
    def fly(self):
        return "Flying at a high altitude."

def let_it_fly(entity):
    print(entity.fly())

let_it_fly(Bird())      # Flying at a moderate height.
let_it_fly(Airplane())  # Flying at a high altitude.

# Polymorphism with Inheritance:

# Base classes define methods, and derived classes override them.
# The overridden method is invoked based on the object type.

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f"Area: {shape.area()}")
