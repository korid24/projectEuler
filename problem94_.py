#https://projecteuler.net/problem=94
from time import time
from math import sqrt
start = time()

def p94(limit):
    x,y = 2,1
    acc = 0
    while True:
        if 2 * x - 1 > limit:
            break
        a = (2 * x - 1) / 3
        area = y * (x - 2) / 3
        if a % 1 == 0 and area % 1 == 0 and a > 1:
            acc += 3 * a + 1


        a = (2 * x + 1) / 3
        area = y * (x + 2) / 3
        if a % 1 == 0 and area % 1 == 0 and a > 1:
            acc += 3 * a - 1

        x,y = 2 * x + y * 3, y * 2 + x
    return acc

print(p94(1000000000))
print( "Time:", time() - start, "Sec.")
