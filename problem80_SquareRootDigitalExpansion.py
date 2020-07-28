#https://projecteuler.net/problem=80
from time import time
from math import sqrt
start = time()

def to_int(l:list):
    strs = [str(x) for x in l]
    return int(''.join(strs))

def to_list(x:int):
    return [int(i) for i in str(x)]

def long_sqrt_digit_sum(x:int):
    l = [int(sqrt(x))]
    operand = x - (int(sqrt(x)) ** 2)
    while len(l) != 100:
        operand *= 100
        left_number = to_int(l) * 2
        for i in range(10)[::-1]:
            subtrahend = to_int(to_list(left_number) + [i]) * i
            if subtrahend <= operand:
                operand -= subtrahend
                l.append(i)
                break
    first = l.pop()
    return sum(to_list(first) + l)

def p80():
    count = 0
    for i in range(2,101):
        if sqrt(i) % 1 != 0:
            count += long_sqrt_digit_sum(i)
    return count

print(p80())


print( "Time:", time() - start, "Sec.")
