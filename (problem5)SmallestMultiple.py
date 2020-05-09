#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def smallestMultiple(n):
    prime_dividers = [i for i in range(2, n + 1) if isPrime(i)]
    max_avalible_pow = [el ** math.floor(math.log(n, el)) for el in prime_dividers]
    ans = 1
    for j in max_avalible_pow:
        ans *= j
    return ans

print(smallestMultiple(20))
