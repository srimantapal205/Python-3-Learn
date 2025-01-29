import utility
from shopping.shopping_cart import buy

print(__name__)
if __name__ == '__main__':
    add = utility.addition(5,5)
    sub = utility.subs(10, 5)
    multi = utility.multi(10,5)
    maxValue= utility.getMaxValue([99,86,12,34,55,67])

    print(add)
    print(sub)
    print(multi)
    print(maxValue)

    buyItem = buy('Apple')
    print(buyItem)
