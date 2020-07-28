#https://projecteuler.net/problem=48
from time import time
start = time()

def self_pow(x):
    acc = 0
    for i in range(1, x+1):
        acc += i**i
    return acc
print(str(self_pow(1000))[-10:])
print( "Time:", time() - start, "Sec.")
