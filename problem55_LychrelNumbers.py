#https://projecteuler.net/problem=55
from time import time
start = time()

def is_palindrome(x:int):
    s = str(x)
    return s == s[::-1]

def rev(x:int):
    return int(str(x)[::-1])

def is_lychrel(x:int):
    n = x
    for i in range(50):
        n += rev(n)
        if is_palindrome(n):
            return False
    return True

def p_55(end):
    count = 0
    for j in range(1,end+1):
        if is_lychrel(j):count+=1
    return count

print(p_55(10000))

print( "Time:", time() - start, "Sec.")
