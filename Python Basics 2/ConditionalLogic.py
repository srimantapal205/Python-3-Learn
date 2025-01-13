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
    