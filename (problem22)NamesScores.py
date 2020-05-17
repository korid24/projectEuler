#https://projecteuler.net/problem=22
from time import time
start = time()

f = open('files/names.txt', 'r')
names_list = ['_'] + sorted(map(lambda el: el.strip('\n').strip('"'), list(f)[0].split(',')))
letters_list = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def name_score(name):
    acc = 0
    for letter in name:
        acc += letters_list.find(letter)
    return acc

def all_names_score(names):
    acc = 0
    for i in range(1, len(names)):
        acc += name_score(names[i]) * i
    return acc

print(all_names_score(names_list))

print( "Time:", time() - start, "Sec.")
