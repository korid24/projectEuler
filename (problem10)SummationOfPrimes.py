#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#Find the sum of all the primes below two million.

def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

def summ_of_primes(end):
    summ = 2
    i = 3
    while i <= end:
        if isPrime(i):
            summ += i
        i += 2
    return summ
print(summ_of_primes(2000000))
