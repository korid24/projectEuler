#https://projecteuler.net/problem=92
from time import time
start = time()

def chain(n:int, processed:list):
    l = [n]
    while l[-1] not in (1,89):
        number = sum([x ** 2 for x in [int(i) for i in str(l[-1])]])
        if processed[number]:
            for el in l:
                processed[el] = processed[number]
            return processed[number]
        l.append(number)
    for el in l[:-1]:
        processed[el] = l[-1]
    return l[-1]

def p93(limit):
    processed = [0] + [None] * (limit-1)
    processed[1], processed[89] = 1,89
    for i in range(2,limit)[::-1]:
        if not processed[i]:
            processed[i] = chain(i,processed)
    return len([x for x in processed if x == 89])

print(p93(10000000))

print( "Time:", time() - start, "Sec.")
