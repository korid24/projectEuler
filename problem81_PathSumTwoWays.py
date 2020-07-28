#https://projecteuler.net/problem=81
from time import time
start = time()

def findpath(matrix):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j-1]
            elif j == 0:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += min(matrix[i][j-1], matrix[i-1][j])
    return matrix[-1][-1]

with open('files/p081_matrix.txt', 'r') as file:
    m = []
    for string in file:
        m.append([int(x) for x in string.split(',')])
    print(findpath(m))


print( "Time:", time() - start, "Sec.")
