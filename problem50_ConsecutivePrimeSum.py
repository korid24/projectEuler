#https://projecteuler.net/problem=50
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def p50(limit):
    primes = [x for x in range(int(limit/2)) if is_prime(x)]
    max_number = 0
    max_count = 0
    for i in range(len(primes) - 1):
        terms = []
        for j in range(i + 1, len(primes)):
            terms = primes[i:j]
            if sum(terms) > limit:
                break
            elif len(terms) > max_count and is_prime(sum(terms)):
                max_count = len(terms)
                max_number = sum(terms)
    return max_number

print(p50(10**6))


print( "Time:", time() - start, "Sec.")
