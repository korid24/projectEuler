#https://projecteuler.net/problem=78
from time import time
start = time()

def make_petns_pairs(lim):
    l = []
    i = 1
    next_element = int(i*(3*i-1)/2)
    while next_element <= lim:
        l+=[(next_element,next_element+i)]
        i+=1
        next_element = int(i*(3*i-1)/2)
    if l[-1][-1] > lim:
        l[-1] = (l[-1][0],)
    return l

def p78():
    p = [1]
    i = 1
    while p[-1] % 1000000:
        pents = make_petns_pairs(i)
        next_element = 0
        for j in range(len(pents)):
            if j % 2 == 0:
                for n in pents[j]:
                    next_element += p[i-n]
            else:
                for n in pents[j]:
                    next_element -= p[i-n]
        p.append(next_element)
        i+=1
    return i-1

if __name__ == '__main__':
    print(p78())
    print( "Time:", time() - start, "Sec.")
