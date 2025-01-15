#while loops structure

# while loop uses a condition to execute a block of code repeatedly until the condition is false
# the condition is checked before the block of code is executed
# the block of code is executed as long as the condition is true
# syntax fo while loop
#  while condition:

#  block of code

i = 0
while i < 50:
    print(i)
    i = i + 1
else:
    print("Done with all the numbers")
    
    
# when should you use a while loop and when should you use a for loop?

listItem = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("Printing list items using for loop")
for i in listItem:
    print(i)
    
    
print("Printing list items using while loop")
i = 0
while i < len(listItem):
    print(listItem[i])
    i+=1
    
    
while True:
    response = input('Say some thing :')
    if (response == 'bye'):
        break


