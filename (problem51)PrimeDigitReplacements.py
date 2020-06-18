#https://projecteuler.net/problem=51
from time import time
from itertools import permutations
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def options(x:int):
    s = str(x)
    cases = []
    for i in range(1, len(s)+1):
        cases += list(map(lambda el:''.join(el), permutations(s + '*'*i)))
    return list(filter(lambda x:x[0] != '0' and x[-1] not in ['0','2','4','6','8'], cases))

def force(s:str):
    if s[0] == '*':
        field = range(1,10)
    else:
        field = range(10)
    d = {'count' : 0, 'list' : []}
    for i in field:
        replaced = int(s.replace('*',str(i)))
        if is_prime(replaced):
            d['count'] += 1
            d['list'].append(replaced)
    return d

def p51(count):
    for number in range(10**6):
        for option in options(number):
            if force(option)['count'] == count:
                return force(option)['list'][0]

print(p51(8))
print( "Time:", time() - start, "Sec.")
