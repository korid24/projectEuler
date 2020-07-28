#https://projecteuler.net/problem=66
from time import time
from math import sqrt
start = time()

def make_cf(n):
    mn = 0
    dn = 1
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convs = [a0]
    if an != sqrt(n):
        trigger = a0 * 2
        while an != trigger:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convs.append(an)
    return convs[:-1]

def cf_inv(cont_fraction):
    numerator = 1
    denominator = cont_fraction.pop()
    while cont_fraction:
        denominator, numerator = denominator * cont_fraction.pop() + numerator, denominator
    return (denominator, numerator)


def find_min_squares(d):
    fraction = make_cf(d)
    if len(fraction) % 2 != 0:
        x,y = cf_inv(fraction)
        x,y = 2 * x ** 2 + 1, 2 * x * y
    else:
        x,y = cf_inv(fraction)
    return x,y

def p66():
    largest = {'x' : 0}
    for i in range(1,1001):
        if sqrt(i) % 1 != 0:
            x,y = find_min_squares(i)
            if x > largest['x']:
                largest = {'x' : x, 'd' : i, 'y' : y}
    return largest

print(p66()['d'])

print( "Time:", time() - start, "Sec.")
