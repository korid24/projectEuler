#https://projecteuler.net/problem=23
from time import time
start = time()

def divisors_sum(n):
    acc = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            acc += [i, int(n / i)]
    return sum(set(acc))

#print(divisors_sum(25))

def isAbundant(x):
    if x < divisors_sum(x):
        return True
    else:
        return False

#print(isAbundant(12))

def nas():
    abudants = [i for i in range(1,28123) if isAbundant(i)]
    all_numbers = [j for j in range(28123)]
    for i in range(len(abudants)):
        for j in range(i,len(abudants) - i):
            if abudants[i]+abudants[j] < 28123:
                all_numbers[abudants[i]+abudants[j]] = 0
            else:
                break
    print(sum(all_numbers))


print(nas())
print( "Time:", time() - start, "Sec.")
