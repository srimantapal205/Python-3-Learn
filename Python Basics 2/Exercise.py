#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for pxs in picture:
    #print(litem)
    for i in pxs:
        #print(i, pxs )
        if(i):
            print('*', end =" ")
        else:
            print(' ', end=" ")
            
    print(' ')
        


picture2 = [
 [0,0,0,0,1,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1]
]
for pxs in picture2:
    for px in pxs:
        if (px):
            print('*', end=" ")
        else:
            print(" ", end=" ")
    print(" ")



pricure3 =[
 [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0] 
]
for pxs in pricure3:
    for px in pxs:
        if px:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print(' ')

pricure4 =[
    [0,0,0,0,1,0,0,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,1,1,1,1,1,0,0],
    [0,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,0],
    [0,0,1,1,1,1,1,0,0],
    [0,0,0,1,1,1,0,0,0],
    [0,0,0,0,1,0,0,0,0]   
]

for pxs in pricure4:
    for px in pxs:
        if px:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print(' ')


picture5 =[
[0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for pxs in picture5:
    for px in pxs:
        if px:
            print('*', end=" ") 
        else:
            print(' ', end=' ')
    print(' ')

picture6 =[
[1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1]
]

for pxs in picture6:
    for px in pxs:
        if px:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print(' ')
picture7 = [
    [1, 1, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 1]
]

for pxs in picture7:
    for px in pxs:
        if px:
            print("*", end =" ")
        else:
            print(" ", end=" ")            
    print(' ')


#Exercise check for duplicates in list
someList = [ 'a', 'b', 'c', 'd', 'b', 'c','e',  ]
duplicates = []
for value  in someList:
    if someList.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)


