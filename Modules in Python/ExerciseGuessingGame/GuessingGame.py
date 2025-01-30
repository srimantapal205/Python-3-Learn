### Generate a number 1~10\n
### input from user\n
### check that input is a number 1~10\n
### Check if number is the right guess. Otherwise ask again.\n

from random import randint

rndmNum = randint(1,10)
# print(rndmNum)


while True:
    try:
        #print(rndmNum)
        guess = int(input("Guess a number 1-10:   "))
        if 0 < guess <11:
            if guess == rndmNum:
                print('You are Genius')
                print('Welcome to Python world')
                break
        else:
            print('Hey, Please enter 1-10! :(')
    except ValueError:
        print("please enter a valid number")
        continue

