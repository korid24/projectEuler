#https://projecteuler.net/problem=95
from time import time
start = time()

def actual(puzzle:list, number:int, position:tuple) -> bool:
    y,x = position
    # check row
    for i in range(len(puzzle[0])):
        if puzzle[y][i] == number and x != i:
            return False
    # check column
    for i in range(len(puzzle)):
        if puzzle[i][x] == number and y != i:
            return False
    # top-left-point of box
    box_x = x // 3
    box_y = y // 3
    # check box
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if puzzle[i][j] == number and (i,j) != (y,x):
                return False
    return True

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

def solve(puzzle):
    empty = find_empty(puzzle)
    if not empty:
        return True
    else:
        x, y = empty

    for i in range(1,10):
        if actual(puzzle, i, (x, y)):
            puzzle[x][y] = i
            # puzzle complete, return 3-digit number in the top left corner
            if solve(puzzle):
                return int(str(sudoku[0][0]) + str(sudoku[0][1]) + str(sudoku[0][2]))
            # wrong
            else:
                puzzle[x][y] = 0
    return False

with open('files/p096_sudoku.txt', 'r') as s:
    sudokus = list(s)
    step = 9
    count = 0
    for i in range(1,len(sudokus), 10):
        text = sudokus[i:i+step]
        sudoku = [[int(x) for x in string.strip()] for string in text]
        count += solve(sudoku)
    print(count)

print( "Time:", time() - start, "Sec.")
