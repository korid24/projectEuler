#https://projecteuler.net/problem=36
from time import time
start = time()

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def dbp(end):
    l = [i for i in range(end) if isPalindrome(i) and isPalindrome(bin(i)[2:])]
    return sum(l)

print(dbp(1000000))
print( "Time:", time() - start, "Sec.")
