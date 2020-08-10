#https://projecteuler.net/problem=89
from time import time
start = time()

def constructor() -> dict:
    hundreds = {1:'C', 5:'D', 10:'M'}
    tens = {1:'X', 5:'L', 10:'C'}
    ones = {1:'I', 5:'V', 10:'X'}
    d = {}
    for block in [hundreds, tens, ones]:
        d[block[1]*5] = block[5]
        d[block[5]*2] = block[10]
        d[block[5] + block[1]*4] = block[1] + block[10]
        d[block[1]*4] = block[1] + block[5]
    return d

replacers = constructor()

def check(roman:str) -> bool:
    for combination in replacers.keys():
        if combination in roman:
            return True
    return False

def minimize(roman:str) -> str:
    minimal = roman
    while check(minimal):
        for old,new in replacers.items():
            minimal = minimal.replace(old,new)
    return minimal

with open('files/p089_roman.txt', 'r') as romans:
    count = 0
    for roman in romans:
        count += len(roman) - len(minimize(roman))
    print(count)

print( "Time:", time() - start, "Sec.")
