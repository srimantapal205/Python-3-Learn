'''
Dunder methods (short for "double underscore methods") in Python, also known as magic methods or special methods, are built-in methods with names surrounded by double underscores (__method__). These methods allow customization of the behavior of Python objects and are used to define how objects behave with built-in operations (like arithmetic, comparisons, or string representation) or language constructs (like iteration).

Categories of Dunder Methods:

Initialization and Object Construction

    Customize how objects are created or destroyed.
        
    Example: __init__, __new__, __del__

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)  # __init__ is automatically called
 
String Representation

    Define how objects are represented as strings.
     Example: __str__, __repr__

class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person(name={self.name})"

p = Person("Alice")
print(p)  # Output: Person(name=Alice)



Arithmetic Operations:

    Overload operators for custom behavior.
    Example: __add__, __sub__, __mul__
    
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
result = v1 + v2  # Calls __add__
print(result.x, result.y)  # Output: 4 6


Comparison Operators

    Customize behavior for comparison operations.
    Example: __eq__, __lt__, __gt__

class Box:
    def __init__(self, volume):
        self.volume = volume
    def __lt__(self, other):
        return self.volume < other.volume

box1 = Box(10)
box2 = Box(20)
print(box1 < box2)  # Output: True

Attribute Access

    Control access to object attributes.
    Example: __getattr__, __setattr__, __delattr__

class Example:
    def __setattr__(self, name, value):
        print(f"Setting {name} to {value}")
        super().__setattr__(name, value)

obj = Example()
obj.attribute = 10  # Output: Setting attribute to 10


Container Behavior

    Make objects behave like containers (lists, dictionaries, etc.).
    Example: __getitem__, __setitem__, __len__

class CustomList:
    def __init__(self, items):
        self.items = items
    def __getitem__(self, index):
        return self.items[index]
    def __len__(self):
        return len(self.items)

clist = CustomList([1, 2, 3])
print(clist[0])  # Output: 1
print(len(clist))  # Output: 3


Iteration:

    Define custom iteration behavior.
    Example: __iter__, __next__

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for num in Counter(1, 3):
    print(num)  # Output: 1, 2, 3

Callable Objects

    Make objects behave like functions.
    Example: __call__

class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greet = Greeter()
print(greet("Alice"))  # Output: Hello, Alice!

Context Managers

    Define behavior for with statements.
    Example: __enter__, __exit__

class Resource:
    def __enter__(self):
        print("Resource acquired")
    def __exit__(self, exc_type, exc_value, traceback):
        print("Resource released")

with Resource():
    print("Using resource")

'''