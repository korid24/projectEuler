#https://projecteuler.net/problem=21
from time import time
start = time()


def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def divisors_sum(n):
    acc = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            acc += [i, int(n / i)]
    return sum(set(acc))

def amicable(x):
    a = divisors_sum(x)
    b = divisors_sum(a)
    if x == b and a != b:
        return a
    else:
        return False

def amicable_numbers_sum(end):
    field = [i for i in range(end+1) if not isPrime(i)]
    acc = 0
    for number in field:
        if amicable(number) in field:
            acc += number + amicable(number)
            field.remove(amicable(number))
    return acc

print(amicable_numbers_sum(10000))

print( "Time:", time() - start, "Sec.")
