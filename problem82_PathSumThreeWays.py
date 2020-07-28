#https://projecteuler.net/problem=82
from time import time
start = time()

def minimal_path(position,prev_updated_column,curr_original_column):
    paths = []
    for i in range(len(prev_updated_column)):
        path = prev_updated_column[i]
        if i <= position:
            path += sum(curr_original_column[i:position+1])
        else:
            path += sum(curr_original_column[position:i+1])
        paths.append(path)
    return min(paths)

def new_column(prev_updated_column,curr_original_column):
    nl = []
    for i in range(len(curr_original_column)):
        nl.append(minimal_path(i,prev_updated_column,curr_original_column))
    return nl

def p82(matrix):
    first_column = [line[0] for line in matrix]
    updated_transposed_matrix = [first_column]
    for i in range(1,len(matrix)):
        new_col = new_column(updated_transposed_matrix[-1], [line[i] for line in matrix])
        updated_transposed_matrix.append(new_col)
    return min(updated_transposed_matrix[-1])

with open('files/p082_matrix.txt', 'r') as file:
    m = []
    for string in file:
        m.append([int(x) for x in string.split(',')])
    print(p82(m))

print( "Time:", time() - start, "Sec.")
