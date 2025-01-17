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


#Positional Argument
say_hey('dff', ':)') #Call or invocking the function

#Keyword Arguments 

say_hey(emoji=':)', name='Baby')


# Default Parameter and Argument

def say_hey_v2(name ='xyz abc', emoji=':)'):
    print(f'Hello {name}, {emoji}')
    
say_hey_v2()
say_hey_v2('wer qwe', ':)')
say_hey_v2('Timmy')


# Return function
'''
In Python, a function with a return statement provides a way to send a result or value back to the caller. The return statement ends the function's execution and specifies what value should be returned to the function's caller.

    Returning a Single Value: The function returns one value to the caller.
    Returning Multiple Values: Python allows functions to return multiple values as a tuple.
    No return Statement: If a function doesn't have a return statement, it implicitly returns

def function_name(parameters):
    # Function logic
    return value


'''
def sum(num1, num2):
    num1 + num2

sum(4,6) # Nothing will print

print(sum(4,6)) #None

def sum_return(num1, num2):
    return num1 + num2

print(sum_return(4,6))

total = sum_return(50, 61)
print(sum_return(100, total))

#Function within in a function


def fun(n1, n2):
    def fun_v2(n1, n2):
        return n1+n2
    return(fun_v2(n1,n2))
print(fun(5,4))


