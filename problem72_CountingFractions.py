#https://projecteuler.net/problem=72
from time import time
start = time()
from sympy.ntheory import factorint
from math import fabs, ceil, floor

def round(x:float):
    if fabs(ceil(x) - x) < fabs(floor(x) - x):
        return ceil(x)
    return floor(x)

def phi(x):
    acc = x
    for num in factorint(x).keys():
        acc *= 1 - 1/num
    return round(acc)

def p72(lim):
    count = 0
    for i in range(2,lim+1):
        count += phi(i)
    return count
print(p72(1000000))

print( "Time:", time() - start, "Sec.")
