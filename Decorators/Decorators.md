# Decorators

Decorators in Python are a powerful and elegant tool to modify or extend the behavior of functions or methods without changing their code. They are a cornerstone of Python’s design, enabling clean and reusable code. Here's a detailed explanation:

### What Are Decorators?

A decorator is essentially a callable (function, method, or class) that takes another function as its argument and extends or alters its behavior. The decorated function is wrapped inside the decorator function, which can perform additional actions before and after calling the original function.

### Syntax of Decorators
    @decorator_function
    def my_function():
        print("Hello, World!")

### How Decorators Work

    def simple_decorator(func):
        def wrapper():
            print("Before the function call")
            func()
            print("After the function call")
        return wrapper

    @simple_decorator
    def say_hello():
        print("Hello!")

    say_hello()

### Types of Decorators

####  Function Decorators

Function decorators extend or modify the behavior of functions or methods.

Example: Logging Decorator
    def logging_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Function '{func.__name__}' is called with {args} and {kwargs}")
            return func(*args, **kwargs)
        return wrapper

    @logging_decorator
    def add(a, b):
        return a + b

    result = add(3, 5)
    print(f"Result: {result}")

#### Class Decorators

Class decorators are used to modify or enhance classes.


    class DecoratorClass:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            print(f"Calling function '{self.func.__name__}'")
            return self.func(*args, **kwargs)

    @DecoratorClass
    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))


### Built-in Decorators

Python provides some built-in decorators for specific use cases:

@staticmethod and @classmethod
Used in classes to define static and class methods, respectively.

@property
Transforms a method into a read-only property.

    class Circle:
        def __init__(self, radius):
            self._radius = radius

        @property
        def radius(self):
            return self._radius

        @radius.setter
        def radius(self, value):
            if value <= 0:
                raise ValueError("Radius must be positive")
            self._radius = value

    c = Circle(5)
    print(c.radius)
    c.radius = 10

### Decorators with Arguments

Decorators themselves can take arguments. This requires nesting an additional layer of functions.


    def repeat_decorator(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    func(*args, **kwargs)
            return wrapper
        return decorator

    @repeat_decorator(times=3)
    def greet(name):
        print(f"Hello, {name}!")

    greet("Alice")


### Chaining Multiple Decorators

You can apply multiple decorators to a single function.

    def decorator1(func):
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)
        return wrapper

    def decorator2(func):
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)
        return wrapper

    @decorator1
    @decorator2
    def say_hello():
        print("Hello!")

    say_hello()


### Use Cases of Decorators
+ Authentication (e.g., @login_required in Flask/Django)
+ Logging and Debugging
+ Timing Function Execution
+ Input Validation
+ Memoization (e.g., @lru_cache)

### Key Points to Remember

**Function Metadata:** Wrapping a function with a decorator replaces its __name__ and __doc__. Use functools.wraps to preserve metadata:

    from functools import wraps

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

**Higher-Order Functions:** Decorators are a form of higher-order functions (functions that take or return functions).

**Reusability:** Decorators encourage clean and reusable code.
