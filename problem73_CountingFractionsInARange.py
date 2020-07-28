#https://projecteuler.net/problem=73
from time import time
from math import ceil, gcd
start = time()

def fractors_count(n):
    bottom, top = ceil(n/3), n // 2 + 1
    return len([x for x in range(bottom,top) if gcd(x,n) == 1])

def p73(lim):
    acc = 0
    for i in range(4,lim+1):
        pass
        acc += fractors_count(i)
    return acc

print(p73(12000))
#Output 7295372
print( "Time:", time() - start, "Sec.")
