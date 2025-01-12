# Tuples 
# Tuples are similar to lists but they are immutable i.e. they cannot be changed.
# Tuples are defined using parentheses () instead of square brackets [].
# Tuples are faster than lists.
# Tuples can be used as keys in dictionaries.
# Tuples are used when the data cannot be changed.

tupleData = (1,2,3,4,5)
print(tupleData)

new_tupleData = tupleData[:]
print(new_tupleData)

x,y,z, *Other = (1,2,3,4,5,6,7,8,9)
print(x)
print(y)
print(z)
print(Other)

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
tupleData = (1,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9,2,3,4,5,2,3,4,2,6,7,4,9)
print(tupleData.count(1))
print(tupleData.index(1))
print(tupleData.count(6)) 
print(len(tupleData)) #length of the tuple