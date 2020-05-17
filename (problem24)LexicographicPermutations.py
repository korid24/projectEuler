#https://projecteuler.net/problem=24
from itertools import permutations
from time import time
start = time()

arr = list(sorted(list(permutations([i for i in range(10)])))[999999])
res = ''.join(map(str, arr))


print(res)
print( "Time:", time() - start, "Sec.")
