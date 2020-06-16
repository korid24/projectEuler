#https://projecteuler.net/problem=49
from itertools import permutations
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def check(l:list):
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            diff = l[j] - l[i]
            if l[j] + diff in l:
                return ''.join(map(str, [l[i], l[j], l[j] + diff]))
    return False

primes = [i for i in range(1488,9999) if is_prime(i)]
for i in primes:
    perms = permutations(str(i))
    perms = [int(''.join(x)) for x in perms]
    perms = list(set([x for x in perms if x in primes]))
    perms.sort()
    if len(perms) >= 3:
        if check(perms):
            print (check(perms))
            break

print( "Time:", time() - start, "Sec.")
