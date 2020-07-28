#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_square_difference(x):
    sumofsquares = sum([i ** 2 for i in range(1, x+1)])
    squareofsum = (sum(range(1, x+1))) ** 2
    return squareofsum - sumofsquares

print(sum_square_difference(10))
print(sum_square_difference(100))
