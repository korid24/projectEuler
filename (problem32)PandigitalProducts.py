#https://projecteuler.net/problem=32
from itertools import permutations
from time import time

start = time()

class CustomSet(set):
    def __str__(self):
        return ''.join(list(self))

    def custom_remove(self:set, s:str):
        for l in s:
            self.remove(l)
        return str(self)


NUMBERS = '123456789'

def is_pandigital(a, b, c):
    input_set = set(str(a) + str(b) + str(c))
    return set(NUMBERS) == input_set

supers = []
for i in sorted(map(lambda x: ''.join(x), permutations(NUMBERS, 2))):
    for j in sorted(map(lambda x: ''.join(x), permutations(CustomSet(NUMBERS).custom_remove(i), 3))):
        product = int(i) * int(j)
        if product > 9876:
            break
        elif is_pandigital(i, j, product):
            supers.append(product)

for i in sorted(map(lambda x: ''.join(x), permutations(NUMBERS, 1))):
    for j in sorted(map(lambda x: ''.join(x), permutations(CustomSet(NUMBERS).custom_remove(i), 4))):
        product = int(i)*int(j)
        if product > 9876:
            break
        elif is_pandigital(i, j, product):
            supers.append(product)
uniques = list(set(supers))

print(sum(uniques))
print( "Time:", time() - start, "Sec.")
