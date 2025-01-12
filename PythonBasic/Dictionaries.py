#Dictionary is a collection of key-value pairs. It is unordered, changeable and indexed.
#Dictionary is represented by curly brackets {}.
#Dictionary is mutable.
#Dictionary is a collection of key-value pairs.

dict_1 = {
    'a': [1,2,3],
    'b': 'Hello',
    'x': True
}

my_list = [
    {
    'a': [1,2,3],
    'b': 'Hello',
    'x': True
    },
    {
    'a': [4,5,6],
    'b': 'World',
    'x': False
    }
]

print(dict_1['a'][1])
print(my_list[1]['a'][0])

# userData = {
#     'ItemList': ['item1', 'item2', 'item3'],
#     'userNmae': 'John',
# }
# print(userData['userAge']) #KeyError: 'userAge' as userAge is not present in the dictionary.
#print(userData.get('userAge')) #None as userAge is not present in the dictionary.
userData = {
    'ItemList': ['item1', 'item2', 'item3'],
    'userNmae': 'John',
    'userAge': 25,
}


print(userData.get('userAge', 50)) #50 as default value  userAge is not present in the dictionary.

'''
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''

userDicData = {
    'ItemList': ['item1', 'item2', 'item3'],
    'userNmae': 'John',
    'userAge': 25,
    }

print(userDicData.items())

new_userData = userDicData.copy()
print(new_userData)

#update() method is used to update the dictionary with the specified key-value pairs.
userDicData.update({'userAge': 30, 'userCity': 'New York'})
#If the key is already present in the dictionary then it will update the value of the key and if the key is not present in the dictionary then it will add the key-value pair in the dictionary.
print(userDicData)


#Remove ITEM from the dictionary using pop() method.
userDicData.pop('userAge')
print(userDicData)

#Remove last item from the dictionary using popitem() method.
userDicData.popitem()
print(userDicData)



#Remove DATA from the dictionary using clear() method.
userDicData.clear()
print(userDicData)