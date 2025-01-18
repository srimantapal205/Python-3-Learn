#Walrus Operator
'''
The walrus operator (:=), introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. It is also called the assignment expression operator. This can make your code more concise and readable by combining an assignment and a test in a single line.

variable := expression
Key Features:
Assigns a value to a variable.
Returns the value, making it usable within the same expression. 

Advantage:
Conciseness: Reduces redundancy in code by combining assignment and usage.
Improved Readability: Keeps related logic close together, especially in loops and conditionals.
Performance: Can save computation by avoiding redundant evaluations.

Limitations:
Scope: The variable assigned using := is scoped to the containing block.
Readability Concerns: Overuse or misuse can make code harder to understand, especially for complex expressions.


'''

x = 'Helloooooooo'
if((n := len(x)) > 10) :
    print(f'{"Too long {n} elements"}')


while ((n := len(x)) > 1):
    print(n)
    x = x[:-1]
    print(x)
    

#Scope

'''
In Python, scope refers to the region of a program where a variable is defined and accessible. Understanding scope is crucial to determine where you can access or modify a variable.

Types of Scope:

Local Scope:
Variables declared inside a function are in the local scope.
They can be accessed only within that function.

Enclosing Scope:
Variables in the enclosing (nonlocal) scope are in a nested function’s outer but not global scope.
The nonlocal keyword is used to modify such variables.

Global Scope:
Variables declared at the top level of a script or outside all functions/classes are in the global scope.
They can be accessed from any part of the code but modified inside a function only using the global keyword.

 Built-in Scope:
Refers to the scope of Python's built-in functions and names (e.g., print, len).
Always available unless overridden by user-defined variables.

Scope Resolution:
Python uses the LEGB Rule to determine variable scope:

Local: Variables inside the current function.
Enclosing: Variables in enclosing functions (nonlocal scope).
Global: Variables declared at the top level of the module.
Built-in: Predefined names in Python.


shadowing:When a variable in a narrower scope (local) has the same name as one in a broader scope (global/enclosing), the local variable shadows the broader one.

'''

def som_fun():
    total = 100 # Functional Scope
#print(total) #NameError: name 'total' is not defined 

x = 10 # Local Scope and this scope can use entire file any-where

def get_value():
    print(x)

get_value()


a = 1

def confu():
    a = 5
    return a

print(a) #1
print(confu()) #5
    

scope = 1 #Global Scope

def parentfun():
    # scope = 11
    def childFun():
        return scope
    return childFun()
print(parentfun())

#1 - scope start with local

#2 - If parent, then check the paren level scope

#3 - Not avaliable in parent an child it will check Global 

#4 - built in python scope


#Global Keyword
print('hello'[0])