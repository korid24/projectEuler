#https://projecteuler.net/problem=70
from sympy.ntheory import factorint
from math import fabs, ceil, floor
from time import time
start = time()

def round(x:float):
    if fabs(ceil(x) - x) < fabs(floor(x) - x):
        return ceil(x)
    return floor(x)

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def is_permutations(x1, x2):
    return sorted(str(x1)) == sorted(str(x2))

def phi(x):
    if is_prime(x):
        return x - 1
    else:
        acc = x
        for num in factorint(x).keys():
            acc *= 1 - 1/num
        return round(acc)

min_n_phi = float('inf')
answear = 0
for i in range(2,10**7+1):
    if not is_prime(i):
        if is_permutations(i, phi(i)):
            if i / phi(i) < min_n_phi:
                min_n_phi = i / phi(i)
                answear = i
print(answear)

print( "Time:", time() - start, "Sec.")
