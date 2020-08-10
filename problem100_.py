#https://projecteuler.net/problem=97
from time import time
start = time()

def p100():
    # all_disks_count
    adc = 21
    # blue_disks_count
    bdc = 15
    while adc < 10**12:
        adc,bdc = 4 * bdc + 3 * adc - 3, 3 * bdc + 2 * adc - 2
    return bdc

print(p100())

print( "Time:", time() - start, "Sec.")
