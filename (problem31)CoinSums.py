#https://projecteuler.net/problem=31
from time import time
start = time()

def ways_count(total):
    ways = [1] + [0] * total
    for coin in [1, 2, 5, 10, 20, 50, 100, 200]:
        for i in range(len(ways) - coin):
          ways[i + coin] += ways[i]
    return str(ways[-1])


print(ways_count(200))
print( "Time:", time() - start, "Sec.")
