#https://projecteuler.net/problem=63
from time import time
start = time()

def lenght(x):
    return len(str(x))

def p63():
    count = 0
    for p in range(1,10**7):
        for n in range(1,10):
            x = n ** p
            if lenght(x) == p:
                count += 1
            elif lenght(x) > p:
                break
            elif lenght(n ** p) < p and lenght((n + 1) ** p) > p:
                return count
print(p63())

print( "Time:", time() - start, "Sec.")
