#https://projecteuler.net/problem=53
from math import comb
from time import time
start = time()

count = 0
for n in range(1,101):
    for r in range(1,n):
        if comb(n,r) > 1000000:
            count += 1
print(count)


print( "Time:", time() - start, "Sec.")
