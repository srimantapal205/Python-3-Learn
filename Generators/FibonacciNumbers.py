# Generate Fibonacci number
# 0,1,1,2,3,5,8,13.........

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a #0
        temp = a
        a = b
        b = temp + b


for x in fib(10):
    print(x)
    
# def fib(number):
#     n1 = 0
#     n2 = 1
#     for i in range(number):
#         yield n1
#         temp = n1
#         n1 = n2
#         n2 = temp + n2


# for x in fib(10):
#     print(x)