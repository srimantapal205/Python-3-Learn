# Error Handling
# https://docs.python.org/3/library/exceptions.html

#In Python, error handling is managed using the try, except, else, and finally blocks. Here's how each of them works:

while True:
    try:
        age = int(input("Enter your age: "))
        10/age
        print(age)
        
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please Enter age higher than 0")
    else:
        print("Thank you")
        break


def sum(num1, num2):
    try:
        return num1 + num2
    except(TypeError, ZeroDivisionError, ValueError) as err:
        print(err)




# print(sum(12, "1")) #unsupported operand type(s) for +: 'int' and 'str'
print(sum(1, 0))


def div(num1, num2):
    try:
        return num1 / num2
    except(TypeError, ZeroDivisionError, ValueError, SyntaxError) as err:
        print(err)
print(div(1, 0))

