#https://projecteuler.net/problem=97
from time import time
from math import sqrt
start = time()

def is_anagram(word1:str, word2:str) -> bool:
    return sorted(word1) == sorted(word2)

def make_squares_anagrams(digits:int) -> list:
    top_border = int(sqrt(10**(digits)))
    botom_border = int(sqrt(10**(digits-1)))
    alls = [str(i**2) for i in range(botom_border-1, top_border+1) if len(set(str(i**2))) == digits]
    groups = []
    for number in alls:
        group = [number]
        for pair in alls:
            if pair != number:
                if is_anagram(number, pair):
                    group.append(pair)
        group.sort(reverse=True)
        if len(group) > 1 and group not in groups:
            groups.append(group)
    final = []
    for group in groups:
        final += group
    final.sort(reverse=True)
    return final

def replacer(pair_of_words:tuple, number:str) -> str:
    word1, word2 = pair_of_words
    number2 = ['0']*len(number)
    for i in range(len(word1)):
        position = word2.index(word1[i])
        number2[position] = number[i]
    return ''.join(number2)


with open('files/p098_words.txt', 'r') as l:
    words = list(l)[0].replace('\"', '').split(',')
    anagrams = []
    for word in words:
        group = [word]
        for pair in words:
            if is_anagram(word, pair) and pair != word:
                group.append(pair)
        group.sort()
        if len(group) > 1 and group not in anagrams:
            anagrams.append(group)

    groups = {}
    for group in anagrams:
        groups[len(group[0])] = []
    for group in anagrams:
        groups[len(group[0])] += [group]

    def p98() -> int:
        for lenght in sorted(groups.keys(), reverse=True):
            squares = make_squares_anagrams(lenght)
            for square in squares:
                for anagrams in groups[lenght]:
                    numbers = []
                    for i in range(len(anagrams)):
                        for j in range(i+1,len(anagrams)):
                            replaced = replacer((anagrams[i],anagrams[j]), square)
                            if replaced in squares:
                                numbers += [square, replaced]
                    if numbers:
                        return int(max(numbers))
    print(p98())


print( "Time:", time() - start, "Sec.")
