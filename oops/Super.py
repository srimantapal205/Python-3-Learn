'''
he super() function in Python is a built-in utility primarily used in object-oriented programming. It allows a subclass to access methods or properties from its parent class. The function simplifies working with inheritance, especially in scenarios involving multiple inheritance or when the parent class’s initialization or method logic needs to be extended.

Features of super()
    Call Parent Class Methods: super() lets you call a method in the parent class without explicitly naming it.
    Simplifies Code in Multiple Inheritance: It ensures the correct method resolution order (MRO) is followed.
    Dynamic Binding: It automatically finds the next class in the MRO, which is especially helpful in diamond inheritance patterns.

super([type[, object-or-type]])

type: The class to start the search for the method.
object-or-type: The object instance or type.


'''

#Basic Use
class Parent:
    def greet(self):
        print('Hello From Parent')
    
    
class child(Parent):
    def greet(self):
        super().greet() #call the parent class's greet method
        print('Hello From Child')

child = child()

child.greet()

print(dir(child))

