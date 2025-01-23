from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def Capitalize(item):
    return item.capitalize()
CapitalizeItem = list(map(Capitalize, my_pets))
print(f'Capitalize Item are: {CapitalizeItem}')


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

zipItem = zip(my_strings, sorted(my_numbers))
listItem = list(zipItem)
print(listItem)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
print(scores)
def filterItem(item):
    return item>50
filterItemList = list(filter(filterItem, scores))
print(f'FilterItem: {filterItemList}')


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def TotalSocre(acc, item):
    return acc+item

TotalScoreValue = reduce(TotalSocre, filterItemList, 0)

print(f'Total Score Value: {TotalScoreValue}')
