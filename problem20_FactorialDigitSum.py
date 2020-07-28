#https://projecteuler.net/problem=20

import math

def FDS(x):
    return sum(map(int, list(str(math.factorial(x)))))

print(FDS(100))
