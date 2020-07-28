#https://projecteuler.net/problem=74
from time import time
from math import factorial
start = time()

def digit_fact(n):
    return sum([factorial(int(x)) for x in str(n)])

def chain_len(x):
    seq = [x]
    next_number = digit_fact(x)
    while next_number not in seq:
        seq.append(next_number)
        next_number = digit_fact(next_number)
    return len(seq)



used = []
count = 0
for i in range(2,1000000):
    if chain_len(i) == 60:
        count += 1

print (count)


print( "Time:", time() - start, "Sec.")
