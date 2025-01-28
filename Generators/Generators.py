'''
A generator in Python is a special type of iterator used to produce a sequence of values lazily, meaning one at a time and only as needed. Generators are implemented using functions that yield values using the yield keyword instead of returning them.

Why Use Generators?
Memory Efficiency: Generators do not store all values in memory at once. Instead, they generate each value on-the-fly, which is ideal for handling large datasets.
Performance: They save time and resources compared to creating and storing large collections like lists.
Infinite Sequences: Generators can represent infinite sequences, as they compute values on demand.

 Creating a Generator:
 Generators are defined like regular functions but use yield to produce values.
def simple_generator():
    yield 1
    yield 2
    yield 3


'''
#time decorator
from time import time
def performance(fn):
    def wrapperFunction(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Its took {t2-t1}s')
        return result
    return wrapperFunction


# @performance
# def long_time():
#     for i in range(100000000):
#         i*5
        
# @performance
# def long_time2():
#     print("2")
#     for i in list(range(100000000)):
#         i*5

# long_time()  
# long_time2()

#Generator function

# def generatorFunction(num):
#     for i in range(num):
#         yield i*2
       
# for item in generatorFunction(100):
#     print(item)

# g = generatorFunction(100)
# print(g)



# # Reguler function 
# def makeList(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result


# list_num = makeList(100)
# print(list_num)


def special_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break
        
special_for([1,2,3])
'''
<list_iterator object at 0x0000025390C56020>
2
<list_iterator object at 0x0000025390C56020>
4
<list_iterator object at 0x0000025390C56020>
6
<list_iterator object at 0x0000025390C56020>
'''



  