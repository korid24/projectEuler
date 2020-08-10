#https://projecteuler.net/problem=97
from time import time
start = time()

pow_of_2 = (2**7830457) % 10000000000
print((28433*pow_of_2 + 1 ) % 10000000000)


print( "Time:", time() - start, "Sec.")
