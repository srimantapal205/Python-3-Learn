lst1 = [1,2,3,4,5,6]
lst2 = ['a','b','c','d','e','f']
lst3 = [1,2,'a',True,3.5]


#List Slicing

cart = ['apple', 'banana', 'cherry', 'date', 'eggfruit', 'fig', 'grape']

print(cart[0])
print(cart[0:2:2])
print(cart[0::2])
print(cart[0:2:2])
print(cart[::-1])
print(cart[-1:2:-2])

cart[0] = 'apricot'
print(cart)


#Matrix
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix2 = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]

matrix2[0][1]

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''


itemList = ['apple', 'banana', 'cherry', 'date', 'eggfruit', 'fig', 'grape']
itemNumber = [1,2,3,4,5,6,7]
#append()	Adds an element at the end of the list
itemList.append('honeydew')
new_Itemlist= itemList
print(f'NewItem List : {new_Itemlist}')
#insert()	Adds an element at the specified position
itemNumber.insert(2, 8)
new_numberSet = itemNumber
print(f'New Number set : {new_numberSet}')

#extend()	Add the elements of a list (or any iterable), to the end of the current list
new_numberSet.extend([9,10,11])
print(f'New Number set : {new_numberSet}')


#Removing Item
new_numberSet.pop()
print(f'After Remove Item - New Number set : {new_numberSet}')

new_numberSet.pop(0) # Remove Item based on Index and can be stored in a variable
print(f'After Remove Item - New Number set : {new_numberSet}')

new_numberSet.remove(5) # Remove Item based on Value
print(f'After Remove Item - New Number set : {new_numberSet}')

new_numberSet.clear() # Clear all the items in the list
print(f'After Clear Item - New Number set : {new_numberSet}')


