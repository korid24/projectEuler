#https://projecteuler.net/problem=47
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

def prime_factors_count(x):
    factors_set = set()
    rest = x
    while not is_prime(rest):
        for i in generate_primes(rest):
            if rest % i == 0:
                rest = int(rest/i)
                factors_set.add(i)
                break
    factors_set.add(rest)
    return len(factors_set)

def pe47(number):
    count = 0
    for i in range(2,10**10):
        if count == number:
            result = i - number
            break
        elif prime_factors_count(i) == number:
            count += 1
        else:
            count = 0
    return result

print(pe47(4))

print( "Time:", time() - start, "Sec.")
