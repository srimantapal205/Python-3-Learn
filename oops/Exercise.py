#Exercise: Cats Everywhere
#Given the  class Cat
# 1 Instantiate the Cat object with 3 cats
# 2 Create a function that finds the oldest cat
# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species ='Mammals'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
cat1 = Cat('cat_1', 5)
cat2 = Cat('cat_2', 7)
cat3 = Cat('cat_3', 9)


def oldest_cat(*args):
    return max(args)

print(f'The oldest cat is {oldest_cat(cat1.age,cat2.age,cat3.age)} years old.')

