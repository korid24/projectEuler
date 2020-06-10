#https://projecteuler.net/problem=44
from time import time
from math import sqrt
start = time()

def generate(x):
    return int(x * (3 * x - 1) / 2)

def is_pentagonal(x):
    return (1 + sqrt(1 + 24 * x)) % 6 == 0

i = 2
run = True
while run:
    for j in range(1,i)[::-1]:
        p1 = generate(i)
        p2 = generate(j)
        if is_pentagonal(p1 - p2) and is_pentagonal(p1 + p2):
            print(p1-p2)
            run = False
            break
    else:
        i += 1

print( "Time:", time() - start, "Sec.")
