#https://projecteuler.net/problem=79
from time import time
start = time()

with open('files/p079_keylog.txt', 'r') as file:
    attempts = [list(string.strip()) for string in file]
    d = {}
    for i in range(10):
        d[str(i)] = set()
    for attempt in attempts:
        d[attempt[0]].add(attempt[1])
        d[attempt[0]].add(attempt[2])
        d[attempt[1]].add(attempt[2])
    max_tail = 0
    for tail in d.values():
        if len(tail)>max_tail:
            max_tail = len(tail)
    password = ''
    for i in range(1,max_tail+1)[::-1]:
        for key,value in d.items():
            if len(value) == i:
                password += key
    password += list(d[password[-1]])[0]
    print(password)


print( "Time:", time() - start, "Sec.")
