
#decorator
from time import time
def performance(fn):
    def wrapperFunction(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Its took {t2-t1}s')
        return result
    return wrapperFunction


@performance
def long_time():
    for i in range(10000000):
        i*5
        

long_time()       