#https://projecteuler.net/problem=69
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def generate_primes():
    return (x for x in range(1000000) if is_prime(x))

def p69(lim):
    acc = 1
    for i in generate_primes():
        if acc * i > lim:
            break
        else:
            acc *= i
    if lim / acc < 2:
        return acc
    else:
        for i in range(int(lim / acc) + 1)[::-1]:
            if is_prime(i):
                return acc * i


print(p69(1000000))
#Output 510510
print( "Time:", time() - start, "Sec.")
