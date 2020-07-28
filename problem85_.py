#https://projecteuler.net/problem=83
from time import time
from math import fabs
start = time()

def rect_count(height, width):
    vars = []
    for h in range(1, height+1):
        for w in range(1,width+1):
            vars.append((h,w))
    count = 0
    for h,w in vars:
        count += (width - w + 1) * (height - h + 1)
    return count

def find_top_border(limit):
    for h in range(1,10**6):
        if rect_count(h,h) > limit:
            return h + 1

def p85(limit):
    min_dif = float('inf')
    width_of_min, height_of_min = 0,0
    for h in range(1,find_top_border(limit)):
        w = h
        value = 0
        while value < limit:
            value = rect_count(h,w)
            if fabs(limit - value) < min_dif:
                min_dif = fabs(limit - rect_count(h,w))
                width_of_min, height_of_min = w,h
            w+=1
    return width_of_min * height_of_min

print(p85(2000000))

print( "Time:", time() - start, "Sec.")
