#https://projecteuler.net/problem=71
from time import time
start = time()

def p71():
    return 3 * 1000000 // 7 - 1

print(p71())

print( "Time:", time() - start, "Sec.")
