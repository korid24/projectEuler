#https://projecteuler.net/problem=38
from time import time
start = time()

def fltr(x:int):
    s = str(x)
    if s[0] != '9': return False
    elif len(set(list(s))) != len(s): return False
    return True

field = [i for i in range(9, 9877) if fltr(i)]

bigestPM = 0
base_of_biggestPM = 0
for number in field:
    acc = str(number)
    n = 2
    while len(acc) < 9:
        acc += str(n*number)
        n += 1
    if fltr(int(acc)) and '0' not in acc:
        if int(acc) > bigestPM:
            bigestPM = int(acc)
            base_of_biggestPM = number

print(bigestPM)

print( "Time:", time() - start, "Sec.")
