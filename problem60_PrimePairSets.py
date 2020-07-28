#https://projecteuler.net/problem=60
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def check(l:list,b):
    for el in l:
        if not is_prime(int(str(el) + str(b))) or not is_prime(int(str(b) + str(el))):
            return False
    return True

def generate_primes(start=3):
    return (x for x in range(start, 10000) if is_prime(x))

def p60():
    for a in generate_primes():
        for b in generate_primes(start=a):
            if check([a], b):
                for c in generate_primes(start=b):
                    if check([a, b], c):
                        for d in generate_primes(start=c):
                            if check([a, b, c], d):
                                for e in generate_primes(start=d):
                                    if check([a, b, c, d], e):
                                        return ([a,b,c,d,e], a+b+c+d+e)
print(p60())
print( "Time:", time() - start, "Sec.")
