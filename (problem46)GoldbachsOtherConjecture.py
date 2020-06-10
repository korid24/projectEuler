#https://projecteuler.net/problem=46
from math import sqrt
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes(x):
    return (i for i in range(x) if is_prime(i))

def goldbach_odd(x):
    for j in generate_primes(x):
        if sqrt((x - j)/2) % 1 == 0:
            return True
    return False

run = True
for n in (i for i in range(33, 10**10,2) if not is_prime(i)):
    if not run:
        break
    elif not goldbach_odd(n):
        print(n)
        run = False
        break


print( "Time:", time() - start, "Sec.")
