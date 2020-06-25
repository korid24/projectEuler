#https://projecteuler.net/problem=58
from time import time
start = time()

def is_prime(x):
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True
# after 1st wrap
primes_count = 3
diagonal_count = 5
position = 9

step = 4
while primes_count / diagonal_count > 0.1:
    for i in range(4):
        position += step
        if is_prime(position):
            primes_count += 1
    step += 2
    diagonal_count +=4
print(position ** 0.5)

print( "Time:", time() - start, "Sec.")
