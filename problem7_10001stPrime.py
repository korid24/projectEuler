#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

def isPrime(x):
    if x < 2:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

def find_in_primes(num):
    count = 1
    operand = 3
    while count < num:
        if isPrime(operand):
            count += 1
        operand += 2
    return (count, operand - 2)

print(find_in_primes(10001))
