#https://projecteuler.net/problem=42
#formula: tn = ½n(n+1) -> n**2 + n - 2tn == 0
from math import sqrt
from time import time
start = time()

f = open('files/p042_words.txt', 'r')
words_list = map(lambda el: el.strip('"'), list(f)[0].split(','))

LETTERS = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def word_score(word:str):
    acc = 0
    for letter in word:
        acc += LETTERS.find(letter)
    return acc

def is_triangle_number(x:int):
    # quadratic equation of the form n**2 + n + q, where q == 2x -> n == (-1 + sqrt(1+8x))/2
    # returs True, if root of the quadratic equation is int
    return sqrt(1 + 8 * x) % 2 == 1

triangles = [word for word in words_list if is_triangle_number(word_score(word))]
print(len(triangles))
print( "Time:", time() - start, "Sec.")
