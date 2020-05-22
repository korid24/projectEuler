#https://projecteuler.net/problem=26
from time import time
import math
start = time()

def make_simple(divisor):
    d = divisor
    while d % 2 == 0 or d % 5 == 0:
        if d % 5 == 0:
            d /= 5
        else:
            d/= 2
    return int(d)

def simples(end):
    simples_set = set(map(make_simple, range(1, end)))
    simlpes_list = list(simples_set)
    simlpes_list.sort()
    return simlpes_list[1:]

def find_period_len(div):
    pow = math.ceil(math.log10(div))
    ans = ''
    unit = 1
    while True:
        ans += str(int(unit*10/div))
        unit = unit*(10**pow) % div
        if len(ans) > 2 and ans[:int(len(ans)/2)] * 2 == ans:
            return int(len(ans)/2)

def longest_period(end):
    workplace = simples(end)
    longest_len = 0
    num = 0
    for number in workplace:
        if find_period_len(number) > longest_len:
            longest_len = find_period_len(number)
            num = number
    return (longest_len, num)

print(longest_period(1000))
print( "Time:", time() - start, "Sec.")
