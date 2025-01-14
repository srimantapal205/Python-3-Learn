#Loop control structure
#break statement
#continue statement
#pass statement

#for loop is iterated over a sequence of items like a list or a string  or a range  or any other iterable object. 
#The loop continues until the last item in the sequence is reached.
#The break statement is used to exit the loop before the last item is reached.
#The continue statement is used to skip the current iteration and move to the next iteration.
#The pass statement is used to do nothing. It is used when a statement is required syntactically but you do not want any command or code to execute.

for item in [1,2,3,4,5]:
    print(item)
    
for item in [1,2,3,4,5,]:
    for i in ['a','b','c','d','e']:
        print(item, i)
#iterable is a sequence of items that can be iterated over. 
#iterable objects include lists, strings, tuples, dictionaries, and sets.
#iterable objects can be used in for loops, list comprehensions, and generator expressions.
#iterable objects can be used in the in operator to check if a value is present in the object.
#iterable objects can be used in the zip function to combine multiple iterables into a single iterable.
#iterable objects can be used in the map function to apply a function to each item in the object.
#iterable objects can be used in the filter function to filter items from the object.
#iterable objects can be used in the sorted function to sort items in the object.

user = {
    'name': 'John',
    'age': 30,
    'email': 'john@user.com',
    'canPaint': True
}

#iterating over a dictionary

for item in user.items():
    print(item)
#items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.
'''
('name', 'John')
('age', 30)
('email', 'john@user.com')
('canPaint', True)
'''
for item in user.values():
    print(item)
#values() method returns a view object that displays a list of a dictionary's values.
'''
John
30
john@user.com
True
'''

for item in user.keys():
    print(item)
#keys() method returns a view object that displays a list of a dictionary's keys.
'''
name
age
email
canPaint

'''

#Another way to iterate over a dictionary is to use the items() method to get a list of key-value pairs and then iterate over the list using a for loop.

for key,value in user.items():
    print(key, ':', value)

'''
name : John
age : 30
email : john@user.com
canPaint : True
'''
sumList = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for item in sumList:
    #sum = sum + item
    sum += item
print('The sum of the list is:', sum)


#range() function is used to generate a sequence of numbers. 
#It takes three arguments: start, stop, and step.
#The start argument is the first number in the sequence.
#The stop argument is the last number in the sequence.
#The step argument is the difference between each number in the sequence.
#The range() function returns a range object that represents the sequence of numbers.
#The range object can be converted to a list using the list() function.
#The range object can be used in a for loop to iterate over the sequence of numbers.

for number in range(0, 10):
    print(number)


# for item in 50:
#     print(item)
# #'int' object is not iterable

# for item in 50:
#     print(item)

#assending order
for _ in range(0, 10, 2):
    print(_)

for _ in range(10, 0, -2):
    print(_)

for _ in range(10, 0, -1):
    print(_)

# enumerate() function is used to add a counter to an iterable object.
#It takes two arguments: iterable and start.
#The iterable argument is the object that you want to add a counter to.
#The start argument is the number that you want the counter to start at.
#The enumerate() function returns a enumerate object that contains the counter and the value of the iterable object.
#The enumerate object can be converted to a list using the list() function.
#The enumerate object can be used in a for loop to iterate over the counter and the value of the iterable object.

for index, value in enumerate(['a', 'b', 'c', 'd', 'e']):
    print(index, value)

for index, value in enumerate(list(range(100))):
    if value == 50:
        print(index, value)
