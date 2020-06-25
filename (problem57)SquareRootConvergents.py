#https://projecteuler.net/problem=57
from time import time
from math import log10 as lg
start = time()

numerator, denominator = 3, 2
count = 0
for i in range(1000):
    numerator, denominator = numerator + 2 * denominator, numerator + denominator
    if int(lg(numerator)) > int(lg(denominator)):
        count += 1
print(count)


print( "Time:", time() - start, "Sec.")
