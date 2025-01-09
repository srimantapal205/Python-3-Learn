# Get string index
selfish = '0123456789'

# [start:stop:stepover]
print(selfish[0:7])
print(selfish[0:7:2])

print(selfish[1:])
print(selfish[::])
print(selfish[:5])
print(selfish[:2:])
print(selfish[-1])
print(selfish[::2])
print(selfish[::-2])


str1 = "Now this idea of immutability is something we'll explore more and more"
print(str1.split(' '))
print(str1.split(' ')[::-1])

# String in python is immutable so we can't change the value of string.


newStr = selfish + str1
print(newStr)