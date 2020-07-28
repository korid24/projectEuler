#https://projecteuler.net/problem=37
from time import time
start = time()

def isPrime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def isTruncatablePrime(x):
    s = str(x)
    for i in range(1,len(s)):
        if not isPrime(int(s[i:])) or not isPrime(int(s[:-i])):
            return False
    return True

generator = (x for x in range(10, 10**999) if isPrime(x))

l = []
for el in generator:
    if isTruncatablePrime(el):
        l.append(el)
    if len(l) == 11:
        break
print(sum(l))

print( "Time:", time() - start, "Sec.")
