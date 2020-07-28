#https://projecteuler.net/problem=67
from time import time
start = time()

def make_pyramid():
    with open('files/p067_triangle.txt', 'r') as source:
        pyramid = []
        for string in source:
            pyramid.append([int(x) for x in string.split()])
        return pyramid

def find_path(pyramid):
    for i in range(len(pyramid) - 1)[::-1]:
        for j in range(len(pyramid[i])):
            pyramid[i][j] += max(pyramid[i+1][j],pyramid[i+1][j+1])
    return pyramid[0][0]

print(find_path(make_pyramid()))

print( "Time:", time() - start, "Sec.")
