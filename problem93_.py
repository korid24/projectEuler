#https://projecteuler.net/problem=93
from time import time
from itertools import combinations,combinations_with_replacement,permutations
start = time()

ALL_DIGITS_COMBINATIONS = list(combinations('123456789', 4))
ALL_OPERATIONS = list(combinations_with_replacement('+-/*', 3))
BRACKETS = (
            '{}{}{}{}{}{}{}',
            '{}{}({}{}{}){}{}',
            '{}{}{}{}({}{}{})',
            '{}{}({}{}{}{}{})',
            '({}{}{}){}({}{}{})',
)

def flat_zip(t1,t2):
    res = []
    for i in range(len(t2)):
        res += [t1[i], t2[i]]
    res.append(t1[-1])
    return tuple(res)

def consecutive_lenght(digit_combination):
    digits_perms = permutations(digit_combination)
    values = set()
    for perm in digits_perms:
        for operations in ALL_OPERATIONS:
            operetions_perms = set(permutations(operations))
            for o_perm in operetions_perms:
                for bracket in BRACKETS:
                    try:
                        value = eval(bracket.format(*flat_zip(perm, o_perm)))
                    except ZeroDivisionError:
                        continue
                    if value > 0 and value % 1 == 0:
                        values.add(value)
    l = sorted(values)
    i = 1
    while l[i] - l[i-1] == 1 and i < len(l):
        i += 1
    return i

def p93():
    max_lenght = 0
    max_lenght_comb = ()
    for combination in ALL_DIGITS_COMBINATIONS:
        if consecutive_lenght(combination) > max_lenght:
            max_lenght = consecutive_lenght(combination)
            max_lenght_comb = combination
    return ''.join(max_lenght_comb)

print(p93())

print( "Time:", time() - start, "Sec.")
