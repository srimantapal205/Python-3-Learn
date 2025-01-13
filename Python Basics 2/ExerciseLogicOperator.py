isMagician = False
isExpert = True

#
# Check if magician AND expert: "You are a master magician"
if isMagician and isExpert:
     print("You are a master magician")
# check if magician but not expert: "At least you're getting there"
elif isMagician and not isExpert:
    print("At least you're getting there")
# if you're not a magician: "You need magic powers"
elif not isMagician:
    print("You need magic powers")