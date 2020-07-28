#https://projecteuler.net/problem=25
from time import time
start = time()

def first(digit):
    a, b = 1, 1
    ind = 2
    while len(str(b)) < digit:
        a, b = b, a + b
        ind += 1
    return ind

print(first(1000))

print( "Time:", time() - start, "Sec.")
