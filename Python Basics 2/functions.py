#A function in Python is a reusable block of code that performs a specific task. It can take inputs (parameters), process them, and return an output.

def say_hello():
    print('Hello World')

say_hello()

'''
In Python, arguments and parameters are related but distinct concepts in the context of functions. Here's a breakdown:

Parameter : 
    Definition: A parameter is a variable defined in the function header (inside parentheses) and acts as a placeholder for the value that will be passed to the function when it is called.

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

Argument: 
    Definition: An argument is the actual value you pass to the function when calling it. It fills in for the parameter.

greet("Alice")  # "Alice" is an argument

Types of Arguments:
    Positional Arguments: Passed in the same order as the parameters.
    Keyword Arguments: Explicitly specify which parameter gets which value.
    Default Arguments: Parameters with default values.
    Variable-Length Arguments: Accept arbitrary numbers of arguments using *args or **kwargs.

'''
def say_hey(name, emoji):
    print(f'Hello {name}, {emoji}')


#Argument
say_hey('dff', ':)') #Call or invocking the function


