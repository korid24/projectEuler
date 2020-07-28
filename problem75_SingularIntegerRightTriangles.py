#https://projecteuler.net/problem=75
from time import time
from math import gcd
start = time()

def primitive_triplets_sums(lim):
    l = []
    for m in range(2,lim//2,2):
        for n in range(1,m,2):
            if 2 * m ** 2 + 2 * m * n > lim:
                break
            elif gcd(m,n) == 1:
                l.append(m**2 - n**2 + 2*m*n + m**2 + n**2)
    for m in range(3,lim//2,2):
        for n in range(2,m,2):
            if 2 * m ** 2 + 2 * m * n > lim:
                break
            elif gcd(m,n) == 1:
                l.append(m**2 - n**2 + 2*m*n + m**2 + n**2)
    return l

def descendants_sums(primitive,limit):
    k = 1
    l = []
    while k * primitive <= limit:
        l.append(k*primitive)
        k+=1
    return l

def all_triplets_sums(lim):
    l = []
    for primitive in primitive_triplets_sums(lim):
        l += descendants_sums(primitive, lim)
    return sorted(l)

def p75(lim):
    field = [0]*(lim+1)
    for i in all_triplets_sums(lim):
        field[i] += 1
    return field.count(1)

print(p75(1500000))


print( "Time:", time() - start, "Sec.")
