#Print the highest even number
def highest_even(li):
    evenList = []
    for  num in li :
         if num % 2 == 0:
            evenList.append(num)
    print(f'EvenList :{evenList}')
    return max(evenList)

listItem = [10,4,5,7.33,60,80,13,67]

print(highest_even(listItem))


