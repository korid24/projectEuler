#https://projecteuler.net/problem=65
from time import time
start = time()

e_seq_start = [2,1]
numerators_start = [2,3]

def make_eseq(lim):
    seq = e_seq_start
    i = 1
    while len(seq) < lim:
        seq += [2*i, 1, 1]
        i += 1
    return seq[:lim]

def p65(position):
    numerators = numerators_start
    for factor in make_eseq(position)[2:]:
        new_numerator = numerators[-2] + numerators[-1]*factor
        numerators.append(new_numerator)
    return sum([int(i) for i in str(numerators[-1])])

print(p65(100))

print( "Time:", time() - start, "Sec.")
