#https://projecteuler.net/problem=29
from time import time
start = time()

def sumpower(n):
    st = str(n)
    return sum([int(i) ** 5 for i in st])
print(sum([j for j in range(10, 1000000) if sumpower(j) == j]))

print( "Time:", time() - start, "Sec.")
