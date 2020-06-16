#https://projecteuler.net/problem=33
from time import time
from math import gcd
start = time()

fractions_prod = [1,1]
for n in range(1,10):
    for i in range(1,10):
        for j in range(1,10):
            if n == j: break
            if eval(f'{i}{n}/{n}{j}') == eval(f'{i}/{j}'):
                fractions_prod[0] *= int(i)
                fractions_prod[1] *= int(j)
print(fractions_prod[1]/gcd(*fractions_prod))
print( "Time:", time() - start, "Sec.")
