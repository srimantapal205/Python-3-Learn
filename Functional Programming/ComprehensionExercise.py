some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


getUnicValue = [item for item in some_list ]
print(getUnicValue)

getDuplicateValue = list(set([item for  item in some_list if some_list.count(item)>1]))

print(getDuplicateValue)