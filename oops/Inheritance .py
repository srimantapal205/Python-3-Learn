'''
Inheritance is a fundamental concept in object-oriented programming (OOP) in Python. It allows a class (called the child class or derived class) to inherit properties and behaviors (methods and attributes) from another class (called the parent class or base class). This enables reusability of code and the ability to build complex systems more efficiently by creating hierarchies of classes.

Concepts of Inheritance in Python:

Parent Class and Child Class:
Parent Class: The class from which properties and methods are inherited.
Child Class: The class that inherits properties and methods from the parent class.

class Parent:
    # Parent class attributes and methods
    pass

class Child(Parent):
    # Child class can have its own attributes and methods
    pass
    
Features of Inheritance
    Access Parent Attributes and Methods: A child class can use all public and protected attributes and methods of the parent class.
    Method Overriding: A child class can redefine methods defined in the parent class.
    Extending Functionality: The child class can add additional methods or attributes while still retaining those of the parent class.

Types of Inheritance :

    # Single Inheritance

    # A child class inherits from one parent class.

    class Parent:
        def greet(self):
            print("Hello from Parent")

    class Child(Parent):
        pass

    obj = Child()
    obj.greet()  # Output: Hello from Parent

    # Multiple Inheritance

    # A child class inherits from more than one parent class.

    class Parent1:
        def greet1(self):
            print("Hello from Parent1")

    class Parent2:
        def farewell1(self):
            print("Goodbye from Parent2")

    class Child1(Parent1, Parent2):
        pass

    obj = Child1()
    obj.greet1()     # Output: Hello from Parent1
    obj.farewell1()  # Output: Goodbye from Parent2



    # Multilevel Inheritance

    # A chain of inheritance where a child class becomes a parent class for another class.

    class Grandparent:
        def greet(self):
            print("Hello from Grandparent")

    class Parent(Grandparent):
        def farewell(self):
            print("Goodbye from Parent")

    class Child(Parent):
        pass

    obj = Child()
    obj.greet()     # Output: Hello from Grandparent
    obj.farewell()  # Output: Goodbye from Parent



    # Hierarchical Inheritance

    # Multiple child classes inherit from a single parent class.

    class Parent:
        def greet(self):
            print("Hello from Parent")

    class Child1(Parent):
        pass

    class Child2(Parent):
        pass

    obj1 = Child1()
    obj1.greet()  # Output: Hello from Parent

    obj2 = Child2()
    obj2.greet()  # Output: Hello from Parent


Method Overriding
When a child class defines a method with the same name as a method in the parent class, the method in the child class overrides the one in the parent class.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):  # Overriding
        print("Hello from Child")

obj = Child()
obj.greet()  # Output: Hello from Child

The super() Function
The super() function is used to call methods of the parent class inside the child class, enabling you to extend the functionality without completely overriding it.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls the Parent's greet method
        print("Hello from Child")

obj = Child()
obj.greet()
# Output:
# Hello from Parent
# Hello from Child


Access Modifiers in Inheritance
Python has three types of access modifiers:

Public: Accessible everywhere.
Protected: Prefixed with a single underscore (_). Accessible within the class and its subclasses.
Private: Prefixed with double underscores (__). Not accessible directly by subclasses but can be accessed using name mangling.

class Parent:
    public_attr = "Public"
    _protected_attr = "Protected"
    __private_attr = "Private"

    def show_private(self):
        return self.__private_attr

class Child(Parent):
    def access_parent_attrs(self):
        print(self.public_attr)       # Accessible
        print(self._protected_attr)   # Accessible
        # print(self.__private_attr)  # Not Accessible
        print(self.show_private())    # Access through method

obj = Child()
obj.access_parent_attrs()
# Output:
# Public
# Protected
# Private



'''