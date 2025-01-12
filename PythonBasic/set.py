# set in python
# set is a collection of unordered and unindexed elements
# set is represented by curly brackets {}
# set is mutable
# set does not allow duplicate elements
# set is used when the order of elements does not matter

myset = {1,2,3,4,5,6,7,8,9,10, 10, 9}
print(myset)

myset.add(11)
myset.add(10)

print(myset)

newItemList = [1,2,3,4,5,6,7,8,9,10, 10, 9]
newSet = set(newItemList)

print(newSet)
print(5 in newSet)
print(15 in newSet)

print(len(newSet))

#conver set to list
print(list(newSet))

newSet2 = newSet.copy()
print(newSet2)

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9,10}
'''
.difference()
.discard()
.differece_update()
.intersection()
.intersection_update()
.isdisjoint()
.issubset()
.issuperset()
.pop()
.remove()
.symmetric_difference()
.symmetric_difference_update()
.union()
.update()

'''
# difference = set1.difference(set2)
# print(difference)

# set1.discard(5)
# print(set1)

# set1.difference_update(set2)
# print(set1)

intersection  = set1.intersection(set2)
print(intersection)

set3 = {1,2,3}
set4 = {4,5,6,7,8,9,10}
isdisjoint = set3.isdisjoint(set4)
print(isdisjoint)