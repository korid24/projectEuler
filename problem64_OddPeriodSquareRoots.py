#https://projecteuler.net/problem=64
from math import sqrt
from time import time
start = time()

def cf(n):
    mn = 0
    dn = 1
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    period = 0
    if an != sqrt(n):
        trigger = a0 * 2
        while an != trigger:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            period += 1
    return period

def p64(lim):
    counter = 0
    for i in range(lim+1):
        if cf(i) % 2 != 0:
            counter += 1
    return counter

print(p64(10000))


print( "Time:", time() - start, "Sec.")
