#https://projecteuler.net/problem=29
from time import time
start = time()

def order_len(lim):
    term_set = set()
    for a in range(2, lim + 1):
        for b in range(2, lim + 1):
            term_set.add(a**b)
    return len(term_set)

print(order_len(100))
print( "Time:", time() - start, "Sec.")
