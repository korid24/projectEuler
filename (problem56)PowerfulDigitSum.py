#https://projecteuler.net/problem=55
from time import time
start = time()

def digit_sum(x:int):
    return sum(map(int, list(str(x))))

def p_50():
    max_sum = 0
    best_a = best_b = 0
    for a in range(1,100):
        for b in range(1,100):
            if digit_sum(a**b) > max_sum:
                max_sum = digit_sum(a**b)
    return max_sum
print(p_50())

print( "Time:", time() - start, "Sec.")
