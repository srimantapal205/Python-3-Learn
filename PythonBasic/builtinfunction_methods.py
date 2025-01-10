'''
str() - converts any data type into a string
int() - converts any data type into an integer
type() - returns the data type of the argument
print() - prints to the console
len() - returns the length of an item

'''

print(len('Now this idea of immutability is something '))

str1 = "Now this idea of immutability is something we'll explore more and more"
print(str1.split(' '))
print(str1.split(' ')[::-1])
print(len(str1.split(' ')[::-1]))

s = str1.split(' ')[::-1]

for i in s:
    print(i)

 

lgs = max(str1.split(' '), key=len)
print(f'{lgs} - {len(lgs) }')

print(f'{lgs.upper()} - {len(lgs) }')
print(f'{lgs.capitalize()} - {len(lgs) }')
print(f'{lgs.lower()} - {len(lgs) }')

print(f'{lgs.find('of')} - {len(lgs) }')




mings = min(str1.split(' '), key=len)
print(f'{mings} - {len(mings) }')


cName= 'Python' 
age = 40  
relationship = 'single'

relationship = 'it\s complicated'

print(f'{relationship}')


birthYear = input('what year were you born? ')
age = 2025 - int(birthYear)
print(f'You will be {age} years old in 2025')

