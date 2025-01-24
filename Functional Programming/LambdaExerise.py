# Generate squre value of given list
squreItemLst = [5,4,3]
squre = lambda item : item ** 2
squreListValue = list(map(squre, squreItemLst)) 
print(squreListValue)

#List sorting  tupple
sItemLst = [(0,2),(4,3),(9,9),(10, -1)]
print(f'Original: {sItemLst}')
lmdSorted = sorted(sItemLst, key=lambda sItemLst: sItemLst[1] )
print(lmdSorted)


#Parameterize
def lambdaSorting(sortedItem):
    return sorted(sortedItem, key=lambda item: item[1])
     
items = [(3, 2), (1, 4), (5, 1),(0,2),(4,3),(9,9),(10, -1)]
sorted_items = lambdaSorting(items)
print(sorted_items)  # Output: [(5, 1), (3, 2), (1, 4)]



