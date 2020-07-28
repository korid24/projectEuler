#https://projecteuler.net/problem=76
from time import time
start = time()

def ways_count(total):
    ways = [1] + [0] * total
    for i in range(1,total):
        for j in range(len(ways) - i):
          ways[i + j] += ways[j]
    return str(ways[-1])

print(ways_count(100))


print( "Time:", time() - start, "Sec.")
