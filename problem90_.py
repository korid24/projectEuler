#https://projecteuler.net/problem=90
from time import time
from itertools import combinations
start = time()

def make_needed_combs() -> tuple:
    combinations_list =[]
    for i in range(1,10):
        sq = ''.join(sorted('{0:0>2}'.format(i**2).replace('9','6')))
        if sq not in combinations_list:
             combinations_list.append(sq)
    return tuple(combinations_list)

NEEDED_COMBS = make_needed_combs()

ALL_CUBES = list(set(combinations('0123456678', 6)))

def count_of(cube1:tuple, cube2:tuple) -> int:
    count = 1
    for cube in [cube1, cube2]:
        if cube.count('6') == 1:
            count *= 2
    combs_of_cubes = set()
    for i in range(6):
        for j in range(6):
            combo = ''.join(sorted(cube1[i] + cube2[j]))
            if combo in NEEDED_COMBS:
                combs_of_cubes.add(combo)
            if len(combs_of_cubes) == len(NEEDED_COMBS):
                return count
    return 0

def p90() -> int:
    count = 0
    for i in range(len(ALL_CUBES)):
        for j in range(i+1):
            count += count_of(ALL_CUBES[i], ALL_CUBES[j])
    return count

print(p90())

print( "Time:", time() - start, "Sec.")
