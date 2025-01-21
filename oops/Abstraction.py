'''
Abstraction in Python:
    Abstraction is a fundamental concept in object-oriented programming (OOP) that simplifies complex systems by hiding unnecessary details and exposing only the essential features. It enables programmers to focus on what an object does instead of how it achieves its functionality. Python provides tools like abstract base classes (ABCs) to implement abstraction.
Features of Abstraction:

    Simplification: By exposing only the relevant methods and properties, abstraction reduces complexity.
    Encapsulation: Hides the implementation details from the user.
    Flexibility: Allows changes to internal implementations without affecting the external interface.
    
Implementing Abstraction:
    Python implements abstraction primarily through:

    Abstract Classes
        An abstract class cannot be instantiated. Instead, it serves as a blueprint for other classes. Abstract classes are defined using the ABC module (Abstract Base Class) from Python's abc package.

    Abstract Methods
        An abstract method is declared in an abstract class but lacks implementation. It must be overridden in the derived class.   


 
'''
from abc import ABC, abstractmethod

# Abstract Class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Concrete Class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Usage
shapes = [
    Rectangle(10, 20),
    Circle(15)
]

for shape in shapes:
    print(f"Area: {shape.area()}, Perimeter: {shape.perimeter()}")
