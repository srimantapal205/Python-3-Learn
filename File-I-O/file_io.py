# file = open("test.txt", "r")  # Open the file in read mode
# myfile = open("test.txt")
# print(myfile)

with open('./data/file.txt', mode='r') as myfile:
    print(myfile.readline())


with open('./data/file.txt', mode='r+') as myfile:
    text = myfile.write('Heay its me :')
    print(text)

with open('./data/file2.txt', mode='w') as myfile:
    text = myfile.write('Hello python  :) ')
    print(text)

try:
    with open('data/err.txt', mode='r') as fileerr:
        print(fileerr.read())
except FileNotFoundError as err:
    print('File does not exit')
    raise  err
