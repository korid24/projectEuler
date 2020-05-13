#https://projecteuler.net/problem=14

def next_element(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

def chain_lenght(frstel):
    operand = frstel
    lenght = 1
    while operand > 1:
        operand = next_element(operand)
        lenght += 1
    return lenght

def longest_chain_under(n):
    start_of_longest = 0
    lenght_of_longest = 0
    for i in range(1, n + 1):
        if chain_lenght(i) > lenght_of_longest:
            start_of_longest = i
            lenght_of_longest = chain_lenght(i)
    return(start_of_longest, lenght_of_longest)

##можно улучшить



print(longest_chain_under(1000000))
