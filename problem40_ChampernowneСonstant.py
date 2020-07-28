#https://projecteuler.net/problem=40
from time import time
start = time()

s = '0'
n = 1
while len(s) < 1000001:
    s += str(n)
    n += 1

result = 1
for i in range(7):
    result *= int(s[10**i])

print(result)
print( "Time:", time() - start, "Sec.")
