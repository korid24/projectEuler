#https://projecteuler.net/problem=88
from time import time
from math import log2, sqrt
start = time()

INFINITY = float('inf')

def product(l:tuple) -> int:
    acc = 1
    for el in l:
        acc *= el
    return acc

def make_number(factors:tuple) -> tuple:
    n = product(factors)
    k = n - sum(factors) + len(factors)
    return n,k

def p88(limit):
    max_count_of_factors = int(log2(limit * 2))
    k_list = [0,0] + [INFINITY] * (limit - 1)
    l =[]
    for i in range(2,limit+1):
        for j in range(2, i+1):
            if i * j > limit * 2:
                break
            else:
                l.append(tuple(sorted([i,j])))
    to_update = l
    size = 2
    while size <= max_count_of_factors:
        sub_set = set()
        for element in to_update:
            for j in range(2, limit+1):
                new_element = tuple(sorted(element+(j,)))
                if product(new_element) > limit * 2:
                    break
                else:
                    sub_set.add(new_element)
        to_update = list(sub_set)
        l += to_update
        size += 1
    n_k = [make_number(x) for x in l if make_number(x)[-1] <= limit]
    for n,k in n_k:
        if k_list[k] > n:
            k_list[k] = n
    return sum(set(k_list))

print(p88(12000))

print( "Time:", time() - start, "Sec.")
