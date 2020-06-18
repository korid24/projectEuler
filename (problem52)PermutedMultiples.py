#https://projecteuler.net/problem=52
from time import time
start = time()

def make_sorted_list(x:int):
    l = list(str(x))
    return sorted(map(int, l))

def p52(x:int):
    for i in range(1,10**10):
        products = []
        for j in range(1,x+1):
            products.append(i*j)
        filtred = filter(lambda el:make_sorted_list(el)==make_sorted_list(i), products)
        if len(list(filtred)) == x:
            return i

print(p52(6))

print( "Time:", time() - start, "Sec.")
