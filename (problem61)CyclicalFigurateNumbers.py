#https://projecteuler.net/problem=60
from time import time
start = time()

def split_number(n):
    return (n//100,n%100)

def make_numbers(formula):
    l = []
    for i in range(1, 10**3):
        x = int(eval(formula.replace('n',str(i))))
        if 999 < x < 10000:
            l.append(x)
        if x > 10000:
            break
    return l

tris = [split_number(x) for x in make_numbers('n*(n+1)/2')]
quad = [split_number(x) for x in make_numbers('n**2')]
pent = [split_number(x) for x in make_numbers('n*(3*n-1)/2')]
hexa = [split_number(x) for x in make_numbers('n*(2*n-1)')]
hept = [split_number(x) for x in make_numbers('n*(5*n-3)/2')]
octo = [split_number(x) for x in make_numbers('n*(3*n-2)')]

alls = [tris, quad, pent, hexa, hept]
def finder():
    for n1 in octo:
        used = [octo]
        array = [n1]
        for field2 in alls:
            for n2 in field2:
                if n2[0] == n1[1] and n2 not in array:
                    used = [octo, field2]
                    array = [n1,n2]

                    for field3 in alls:
                        if field3 not in used:
                            for n3 in field3:
                                if n3[0] == n2[1] and n3 not in array:
                                    used = [octo, field2, field3]
                                    array = [n1,n2,n3]

                                    for field4 in alls:
                                        if field4 not in used:
                                            for n4 in field4:
                                                if n4[0] == n3[1] and n4 not in array:
                                                    used = [octo, field2, field3,\
                                                    field4]
                                                    array = [n1,n2,n3,n4]

                                                    for field5 in alls:
                                                        if field5 not in used:
                                                            for n5 in field5:
                                                                if n5[0] == n4[1]\
                                                                and n5 not in array:
                                                                    used = [octo,\
                                                                    field2, field3, field4, field5]
                                                                    array = [n1,n2,n3,n4,n5]

                                                                    for field6 in alls:
                                                                        if field6 not in used:
                                                                            for n6 in field6:
                                                                                if n6[0] == n5[1]\
                                                                                and n6[1] == n1[0]\
                                                                                and n6 not in array:
                                                                                    return\
                                                                                    [n1,n2,n3,n4,n5,n6]

def p61():
    return sum([el[0]*100 + el[1] for el in finder()])

print(p61())

print( "Time:", time() - start, "Sec.")
