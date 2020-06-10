#https://projecteuler.net/problem=43
from itertools import permutations
from time import time
start = time()

def unite(t:tuple):
    return ''.join(t)

NUMBERS = '0123456789'

def it_appropriate(s:str):
    divisors = [2,3,5,7,11,13,17]
    for i in range(1,8):
        if int(s[i:i+3]) % divisors[i-1] != 0:
            return False
    return True

perms = [i for i in map(lambda el:unite(el), permutations(NUMBERS)) if i[0] != '0' and it_appropriate(i)]
print(sum(map(int, perms)))
print( "Time:", time() - start, "Sec.")
