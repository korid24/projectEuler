#https://projecteuler.net/problem=28
from time import time
start = time()

def spiral_diagonals_sum(size):
    #biggest number
    n = size ** 2
    #step between biggest "lap" angles
    step = size - 1
    acc = 1
    while n > 1:
        for i in range(4):
            acc += n
            n -= step
            #print(n)
        step -= 2
    return acc

print(spiral_diagonals_sum(1001))
print( "Time:", time() - start, "Sec.")
