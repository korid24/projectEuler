#https://projecteuler.net/problem=39
import math
from time import time
start = time()

def isTriplet(x):
    for m in range(1,int(x ** 0.5)):
        for n in range(1,m):
            if m ** 2 + m * n == x / 2:
                return True
    return False


def tripletsCount(x):
    count = 0
    for a in range(1,int(x/3)):
        for b in range(a, int(x/2)):
            if math.hypot(a,b) + a + b == x:
                count += 1
    return count

def max_solutions(end):
    field = (x for x in range(end + 1) if isTriplet(x))
    max_count = 0
    p_of_max = 0
    for number in field:
        if tripletsCount(number) > max_count:
            max_count = tripletsCount(number)
            p_of_max = number
    return (max_count, p_of_max)

print(max_solutions(1000))
print( "Time:", time() - start, "Sec.")
