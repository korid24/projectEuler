#https://projecteuler.net/problem=35
from time import time
start = time()

def isPrime(x):
    if x <= 0: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def isCircularPrime(n):
    s = str(n)
    for i in range(len(s) - 1):
        s = s[-1] + s[:-1]
        if not isPrime(int(s)):
            return False
    return True

def circularPrimesCount(end):
    count = 0
    for j in [i for i in range(2, end+1) if isPrime(i)]:
        if isCircularPrime(j):
            count += 1
    return count

print(circularPrimesCount(1000000))
print( "Time:", time() - start, "Sec.")
