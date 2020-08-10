#https://projecteuler.net/problem=86
from time import time
from math import sqrt
start = time()

def shortest_way(width, lenght_height):
    return sqrt(width ** 2 + lenght_height ** 2)

def p86(lim):
    count = 0
    w = 1
    while count < lim:
        w += 1
        for lh in range(2,2*w):
                    if shortest_way(w,lh) % 1 == 0:
                        if lh <= w:
                            count += lh // 2
                        else:
                            count += 1 + (w - (lh + 1) // 2)
    return w
print(p86(1000000))


print( "Time:", time() - start, "Sec.")
