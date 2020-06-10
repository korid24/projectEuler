#https://projecteuler.net/problem=45
from time import time
from math import sqrt
start = time()

def generate_hexagonal(x:int):
    return x * (2 * x - 1)

def is_pentagonal(x:int):
    return (1 + sqrt(1 + 24 * x)) % 6 == 0

for i in range(144, 10**10):
    n = generate_hexagonal(i)
    # all hexagonals is triangles
    if is_pentagonal(n):
        print(n)
        break

print( "Time:", time() - start, "Sec.")
