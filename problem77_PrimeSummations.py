#https://projecteuler.net/problem=77
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def prime_generator(limit):
    return (x for x in range(limit) if is_prime(x))

def ways_count(total):
    ways = [1] + [0] * total
    for prime in prime_generator(total):
        for i in range(len(ways) - prime):
          ways[i + prime] += ways[i]
    return ways[-1]

def p77(x):
    for i in range(5,10**6):
        if ways_count(i)>x:
            return i
print(p77(5000))


print( "Time:", time() - start, "Sec.")
