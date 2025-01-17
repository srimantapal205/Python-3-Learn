
#Methods vs function
'''
In Python, methods and functions are similar in that both are blocks of reusable code, but they have some key differences in how they are associated with objects and how they are called.

Function:
    Definition: A block of code that is defined using the def keyword and can be called independently.
    Associated With: Not bound to any object.
    Scope: Functions can be defined globally or locally within another function.
    How to Call: Functions are called by their name, optionally passing arguments.
    
    def greet(name):
    return f"Hello, {name}!"
    print(greet("Alice"))  # Output: Hello, Alice!

Method:
    Definition: A function that is associated with an object. Methods are functions that are part of a class and operate on instances of that class.
    Associated With: Bound to an object (instance or class).
    Scope: Defined inside a class.
    How to Call: Methods are called on an object using the object.method() syntax.

    class Greeter:
    def greet(self, name):
        return f"Hello, {name}!"

    greeter = Greeter()
    print(greeter.greet("Alice"))  # Output: Hello, Alice!


Types of Methods:
    Instance Methods: Operate on an instance of the class; the first parameter is self
    Class Methods: Operate on the class itself; the first parameter is cls.
    Static Methods: Do not operate on the instance or class; no special first parameter.
    
'''


#function info seeting

def test(a):
    '''
    Info : This function work for the diffrent.......
    '''
    print(a)

test('!!!')

help(test)

print(test.__doc__)


#Clean Code
def is_EvenNum(num):
    return num % 2 == 0
print(is_EvenNum(50))
print(is_EvenNum(51))

#Find the long word

def long_word(sentence):
    leargWord = max(sentence.split(' '), key=len)
    return leargWord

print(long_word('Types of Methods'))

# *args **kwargs

def super_fun(*args):
    print(args)
    return sum(args)

print(super_fun(1,2,3,4,5))

def super_fun(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_fun(1,2,3,4,5, num1 = 5, num2= 10))

#rule : Params, *args, default parameters, **kwargs

## def super_fun(name, *args, i='hi', **kwargs):
     