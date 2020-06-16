#https://projecteuler.net/problem=34
from time import time
from math import factorial
start = time()

def is_curious(x:int):
    l = map(int, list(str(x)))
    return sum(map(factorial, l)) == x

numbers = [i for i in range(3,150000) if is_curious(i)]
print(sum(numbers))

print( "Time:", time() - start, "Sec.")
