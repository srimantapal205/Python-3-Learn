#Conditional statements IF, ELIF, ELSE
#IF statement
isOld = False
isLicenced = True

if isOld:
    print("You are old enough to drive")
else:    
    print("You are not old enough to drive")


if isOld:
    print("You are old enough to drive")
elif isLicenced:
    print("You are licenced")
else:    
    print("Ok Ok !")
    

isOld = True
isLicenced = True
if isOld and isLicenced:
    print("You are old enough to drive and you have licence !")
else:    
    print("You are not old enough to drive")
   
   
# Truthy and Falsy values
# falsy values
'''
None
False
Numbers that are numerically equal to zero, including:
0
0.0
0j
decimal.Decimal(0)
fraction.Fraction(0, 1)
Empty sequences and collections, including:
[] - an empty list
{} - an empty dict
() - an empty tuple
set() - an empty set
'' - an empty str
b'' - an empty bytes
bytearray(b'') - an empty bytearray
memoryview(b'') - an empty memoryview
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0, given that obj.__bool__ is undefined
 
 '''
 
 
 #Ternary Operator 
 # condition_if_true if condition else condition_if_false
isFriend = True
canMessage = "message allowed" if isFriend else "message not allowed"
print(canMessage)

# Short Circuiting
isUser = True
isFriend = True
if isUser or isFriend:
    print("Best Friends Forever")
    

#Logical Operators
# and, or, not, >, <, >=, <=, ==, !=
print(0 and 1)#
print(0 or 1)#
print(not 0)#
print(not 1)#
print(0 > 1)#
print(0 < 1)#
print(0 >= 1)#
print(0 <= 1)#
print(0 == 1)#
print(0 != 1)#
print(0 == 0)#False
print(0 != 0)#True
print(0 is 0) #True


print('a' > 'A')
#why 'a' > 'A' is true?
#ASCII values of 'a' and 'A' are 97 and 65 respectively.
print('Coditional Value')
print(1<2<3<4)
print(1>2<3>4)
print(1>=2<=3>=4)
print(1<=2>=3<=4)

#NOT operator 
#It is used to reverse the logical state of its operand and return oposite value.
print('NOT operator')
print(not(False))
print(not(True))
