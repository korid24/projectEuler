#https://projecteuler.net/problem=62
from time import time
start = time()

cubes_nums = []

for i in range(10**10):
    current_cube_nums = sorted(str(i**3))
    cubes_nums.append(current_cube_nums)
    if cubes_nums.count(current_cube_nums) == 5:
        print(cubes_nums.index(current_cube_nums) ** 3)
        break

print( "Time:", time() - start, "Sec.")
