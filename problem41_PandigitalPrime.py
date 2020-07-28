#https://projecteuler.net/problem=41
from itertools import permutations
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def unite(t:tuple):
    return int(''.join(t))

NUMBERS = '123456789'

for i in range(1,9):
    vars = permutations(NUMBERS[:-i])
    primes = [i for i in map(lambda el:unite(el), vars) if is_prime(i)]
    if primes:
        print(max(primes))
        break
print( "Time:", time() - start, "Sec.")
