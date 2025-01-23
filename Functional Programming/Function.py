# Pure Function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

multiply = multiply_by2([1,2,3,4,5])
print(multiply)

#map() Function
'''
The map() function in Python is a built-in higher-order function used to apply a given function to each item of an iterable (e.g., list, tuple) and return a map object (an iterator) with the results. It's a key part of functional programming in Python.

map(function, iterable, ...)


'''
print(map(multiply_by2, [5,6,7,8,9] )) # return <map object at 0x0000014E5ABD5B40> as memory address.
# print(list(map(multiply_by2, [5,6,7,8,9]) )) # Error 'int' object is not iterable 

mLst = [4,5,6,7]
def multipleByNnumber(ls):
    #Parameterize multiply
        return ls*2
    
FunctionValue = list(map(multipleByNnumber, [9,8,7,6,5]))        
print(FunctionValue)

pureFunctionValue = list(map(multipleByNnumber, mLst))  
print(pureFunctionValue) # Map create a hole new list and it's not touch the out side world
print(mLst) # the Original function is not modifyed, that means it's a immutable     


#filter() Function:
'''
The filter() function in Python is a built-in function used to filter elements from an iterable based on a condition specified by a function. It returns a new iterable containing only the elements for which the condition evaluates to True.

filter(function, iterable)


'''

def checkOdd(item):
    return item%2 != 0
nItem= [1,2,3,4,5,6,7,8,9]
FilterOddValue = list(filter(checkOdd, nItem))        
print(FilterOddValue)
print(nItem)


#zip() Function:

'''
The zip() function in Python is a built-in utility that combines elements from two or more iterables (e.g., lists, tuples, strings) into tuples. It essentially "zips" the iterables together, element by element.

zip(*iterables)

*iterables: One or more iterables (e.g., lists, tuples, strings).
Returns: An iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
    
'''
z1Item = [10,20,30]
z2Item = [1,2,3]
zipItem = zip(z1Item, z2Item)
print(list(zipItem)) [(10, 1), (20, 2), (30, 3)]