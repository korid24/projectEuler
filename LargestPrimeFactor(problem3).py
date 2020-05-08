#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
def isPrime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

#print(isPrime(4))

def largest_prime_factor(n):
    count = n
    i = 1
    while count > 1:
        i += 1
        if isPrime(i) and count % i == 0:
            count /= i
    return i



print(largest_prime_factor(600851475143))
