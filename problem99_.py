#https://projecteuler.net/problem=97
from time import time
from math import log10 as lg
start = time()

def is_bigger(last_biggest:tuple, new:tuple) -> bool:
    biggest_base,biggest_pow = last_biggest
    new_base,new_pow = new
    return new_pow * lg(new_base) > biggest_pow * lg(biggest_base)

def unpack(l:list) -> tuple:
    base,pow = l
    return int(base), int(pow)

with open('files/p099_base_exp.txt','r') as file:
    bases_and_pows = [unpack(s.strip().split(',')) for s in file]
    biggest = bases_and_pows[0]
    position = 0
    for i in range(1,len(bases_and_pows)):
        if is_bigger(biggest, bases_and_pows[i]):
            biggest = bases_and_pows[i]
            position = i
    print(position + 1)

print( "Time:", time() - start, "Sec.")
