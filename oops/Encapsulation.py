'''
Encapsulation is one of the fundamental principles of object-oriented programming (OOP). It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class. Encapsulation also involves restricting direct access to some of an object's components, which is a mechanism to safeguard the integrity of the data.

In Python, encapsulation is implemented through the use of access modifiers (public, protected, and private) and by defining methods that control access to the internal state of an object.

Access Modifiers:

Python uses naming conventions to define the accessibility of variables and methods:

Public: Attributes and methods that are accessible from anywhere.
class MyClass:
    def __init__(self):
        self.public_var = "I am public"
    
    def public_method(self):
        return "This is a public method"

obj = MyClass()
print(obj.public_var)  # Accessible
print(obj.public_method())  # Accessible

Protected: Attributes and methods intended to be accessed only within the class and its subclasses. Indicated by a single underscore prefix (_).
class MyClass:
    def __init__(self):
        self._protected_var = "I am protected"
    
    def _protected_method(self):
        return "This is a protected method"

obj = MyClass()
print(obj._protected_var)  # Accessible, but should be used cautiously
print(obj._protected_method())  # Accessible, but not recommended

Private: Attributes and methods that cannot be accessed directly from outside the class. Indicated by a double underscore prefix (__).
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"
    
    def __private_method(self):
        return "This is a private method"

obj = MyClass()
# print(obj.__private_var)  # AttributeError
# print(obj.__private_method())  # AttributeError

# Accessing private attributes using name mangling
print(obj._MyClass__private_var)  # Works, but discouraged

Getter and Setter Methods
To maintain control over how attributes are accessed and modified, Python provides the concept of getter and setter methods.

Getter: Retrieves the value of an attribute.
Setter: Updates the value of an attribute with validation or additional logic.

class MyClass:
    def __init__(self):
        self.__private_var = "Initial Value"
    
    def get_private_var(self):
        return self.__private_var
    
    def set_private_var(self, value):
        if isinstance(value, str):  # Example of validation
            self.__private_var = value
        else:
            raise ValueError("Value must be a string")
    
obj = MyClass()
print(obj.get_private_var())  # Access via getter

obj.set_private_var("New Value")  # Modify via setter
print(obj.get_private_var())


Using the @property Decorator
Python provides a more elegant way to implement getters and setters using the @property decorator. It allows you to define a method that can be accessed like an attribute.

class MyClass:
    def __init__(self):
        self.__private_var = "Initial Value"
    
    @property
    def private_var(self):
        return self.__private_var
    
    @private_var.setter
    def private_var(self, value):
        if isinstance(value, str):
            self.__private_var = value
        else:
            raise ValueError("Value must be a string")
    
obj = MyClass()
print(obj.private_var)  # Access like an attribute

obj.private_var = "New Value"  # Modify like an attribute
print(obj.private_var)

Benefits of Encapsulation:
    Data Hiding: Protects sensitive data by restricting direct access.
    Data Integrity: Ensures attributes can only be modified in a controlled manner.
    Improved Maintainability: Changes to the internal implementation don't affect external code.
    Flexibility: Allows additional logic (e.g., validation) when accessing or modifying data.
'''

