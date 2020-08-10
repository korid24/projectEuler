#https://projecteuler.net/problem=91
from time import time
from  math import sqrt
start = time()

def is_rihgt(x1,x2,y1,y2):
    first = x1 ** 2 + y1 ** 2
    second = x2 ** 2 + y2 ** 2
    third = (x2-x1)**2 + (y2-y1) ** 2
    l = sorted([first, second, third])
    return l[0] + l[1] == l[2]

def p91(size):
    count = 0
    for x1 in range(size+1):
        for y1 in range(size+1):
            for x2 in range(size+1):
                for y2 in range(size+1):
                    if (0,0) in ((x1,y1), (x2,y2)) or (x1,y1) == (x2,y2):
                        continue
                    elif is_rihgt(x1,x2,y1,y2):
                        count += 1
    return count / 2

print(p91(50))

print( "Time:", time() - start, "Sec.")
