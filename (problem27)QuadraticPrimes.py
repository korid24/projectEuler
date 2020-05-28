#https://projecteuler.net/problem=27
from time import time
start = time()

def isPrime(x):
    if x <= 0: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def primes_count(a, b):
    n = 0
    while isPrime(n**2 + a*n + b):
        n += 1
    return n

def quadratic_primes(end):
    b_field = [i for i in range(2,end) if isPrime(i)]
    max_count = 0
    for b in b_field:
        for a in range(-b,b, 2):
            if primes_count(a,b) > max_count:
                best_a = a
                best_b = b
                max_count = primes_count(a,b)
    return best_a * best_b

print(quadratic_primes(1000))
print( "Time:", time() - start, "Sec.")
