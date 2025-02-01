# List Comprehension
'''
[expression for item in iterable if condition]
expression: The value or transformation applied to each item.
iterable: The source sequence to iterate over.
condition (optional): A filter to include only certain items.
'''

strinhHelo = [char for char in 'HelloWorld']
print(strinhHelo)



newList = [item for item in range(0,100)]
print(newList)

#action based
newList2 = [item**2 for item in range(0, 100)]
print(f'Number Power List :: {newList2}')

#get Even No
evenNoList = [item for item in newList2 if item%2 == 0]
print(f'Even No List: {evenNoList}')

# Set Comprehension
'''
Set Comprehension in Python is a concise way to create sets by applying transformations or filtering conditions to elements from an iterable. It uses curly braces {} and works similarly to list comprehensions, but it automatically removes duplicates since sets only contain unique elements.

{expression for item in iterable if condition}

'''
setStr =  {char for char in 'Helloword'}
print(setStr)

setNewList = {item for item in range(0,100)}
print(setNewList)

#Set action based
setNewList2 = {item**2 for item in range(0,100)}
print(setNewList2)

#Get set even list
setevenList = {item for item in setNewList2 if item %2 == 0}
print(setevenList)

# Get unique number
numLists = [1,2,1,4,3,5,3,4,7,9,7,6,0,4,5,1,2,3,4,5,5,6,6,7,8,9,0,1,2,3,2,4,3,5,4,5,6,5,7,8,8]
getUnicValue = {item for item in numLists}
print(getUnicValue)

# Dictionary Comprehension 
'''
Dictionary Comprehension in Python is a concise way to create dictionaries by transforming or filtering items from an iterable. It allows you to build dictionaries with keys and values using a single line of code.
'''

## {key_expression: value_expression for item in iterable if condition}

'''
key_expression: Defines the keys of the dictionary.
value_expression: Defines the values of the dictionary.
iterable: The sequence to iterate over.
condition (optional): Filters the items to include in the dictionary.

'''

dicSqure = {x: x**2  for x in range(0,20)}
print(dicSqure)
  
simpleDict = {
    'a':1,
    'b':2
}  
    
newDict = {key:value**2 for key,value in simpleDict.items() }

print(newDict)

kvlst = [1,2,3]

newKVlst = {x : x *2 for x in kvlst}
print(newKVlst)

from collections import Counter
elements = [1,2,3,1,2,3,4,5,1,2,3,2,2]
# Count occurrences of each element
element_counts = Counter(elements)
# Extract repeated elements
repeated_elements = [item for item in elements if element_counts[item] > 1]
print(repeated_elements)

def getAllRepeatItem(item):
    ri = []
    for i in item:
        if item.count(i) > 1:
            ri.append(i)
    return ri
        
        
        
        
elements2 = [1,2,3,1,2,3,4,5,1,2,3,2,2]     
print(getAllRepeatItem(elements2))   

def GetOnlyRepetedItem(item):
    reptdItem =[]
    
    for i in item:
        if item.count(i)>1:
              if i not in reptdItem:
                    reptdItem.append(i)
    return reptdItem               

print(GetOnlyRepetedItem(elements2))