#Decorator
# Decorator provide extra featue inside the function. and It's very powerfull 
# Also call this decrator function


    
def my_decorator(func):
    def wrap_function(x):
        print('******')
        func(x)
        print('******')
    return wrap_function


# @my_decorator
# def hello():
#     print('helloooo')


# def bye():
#     print('See you later...')


# hello()


@my_decorator
def helloParam(greeting):
    print(greeting)


helloParam('Hiii')

#Decorator with multiple arguments
def  multiPleDecorator(function):
    def wrapperFunction(*args, **kwargs):
        print('*******************')
        function(*args, **kwargs)
        print('*********************')
    return wrapperFunction
#using first class and high order function
@multiPleDecorator
def hello(gretting, emoji):
    print(gretting, emoji)

hello('Hiii.....',':)')

#first class and higher order function with default argument
@multiPleDecorator
def helloWorld(grtting='Hi...', emoji=':)'):
    print(grtting, emoji)

#Pass default value
helloWorld()

#Pass parameter values
helloWorld('Hi---- Guyes', ':(')
