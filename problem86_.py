#https://projecteuler.net/problem=83
from time import time
from '\(problem78\)CoinPartitions' import make_petns_pairs as mpp
start = time()

def shortest_way(cuboid):
    width, height, lenght = cuboid
    return sqrt(width ** 2 + (lenght + height) ** 2)

def p86(target):
    for i in range(1, 10**6):
        count = 0
        for h in range(1,i):
            for l in range(h,i):
                for w in range(l,i):
                    cub = (w,h,l)
                    if shortest_way(cub) % 1 == 0:
                        count += 1
                        if count > target:
                            return max([l,w,h]), count

print(p86(2000))

print( "Time:", time() - start, "Sec.")
