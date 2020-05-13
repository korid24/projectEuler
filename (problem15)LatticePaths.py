#https://projecteuler.net/problem=15

import math

def count_of_path(grid_side):
    needed_steps = grid_side * 2
    one_direction_steps = needed_steps / 2
    return int(math.factorial(needed_steps) / math.pow(math.factorial(one_direction_steps), 2))

print(count_of_path(20))
