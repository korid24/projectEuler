#https://projecteuler.net/problem=83
from time import time
from heapq import heapify, heappush, heappop
start = time()

def set_children(value,coordinates,updated_matrix, matrix):
    lenght = len(updated_matrix)
    x,y = coordinates
    l = []
    if x + 1 < lenght and not updated_matrix[y][x+1]:
        min_path = matrix[y][x+1] + value
        updated_matrix[y][x+1] = min_path
        l.append([min_path, (x+1,y)])
    if y - 1 >= 0 and not updated_matrix[y-1][x]:
        min_path = matrix[y-1][x] + value
        updated_matrix[y-1][x] = min_path
        l.append([min_path, (x,y-1)])
    if y + 1 < lenght and not updated_matrix[y+1][x]:
        min_path = matrix[y+1][x] + value
        updated_matrix[y+1][x] = min_path
        l.append([min_path, (x,y+1)])
    if x - 1 >= 0 and not updated_matrix[y][x-1]:
        min_path = matrix[y][x-1] + value
        updated_matrix[y][x-1] = min_path
        l.append([min_path, (x-1,y)])
    return l

def p83(mat):
    size = len(mat)
    upd_matrix = [[None for i in range(size)] for j in range(size)]
    upd_matrix[0][0] = mat[0][0]
    heap = [[upd_matrix[0][0], (0,0)]]
    heapify(heap)
    while len(heap) != 0:
        value, coordinates = heappop(heap)
        for child in set_children(value, coordinates, upd_matrix, mat):
            heappush(heap, child)
    return upd_matrix[-1][-1]

with open('files/p082_matrix.txt', 'r') as file:
    m = []
    for string in file:
        m.append([int(x) for x in string.split(',')])
    print(p83(m))

print( "Time:", time() - start, "Sec.")
