#https://projecteuler.net/problem=95
from time import time
start = time()

def divisors_sums(top_border:int) -> list:
    numbers = [0] + [1 for _ in range(top_border)]
    for i in range(2,top_border+1):
        for n in range(2, top_border//i + 1):
            numbers[i*n] += i
    return numbers

def p95(limit:int) -> int:
    divs = divisors_sums(limit)
    stop_list = []
    for element in divs:
        stop_list.append(element <= 1)

    def chain_lenght(n:int) -> tuple:
        chain = [n]
        while divs[chain[-1]] not in chain:
            next_element = divs[chain[-1]]
            if next_element > len(divs) or stop_list[next_element]:
                for element in chain:
                    stop_list[element] = True
                return -1,-1
            else:
                chain.append(next_element)
        for element in chain:
            stop_list[element] = True
        if divs[chain[-1]] == n:
            return n, len(chain)
        else:
            next_element = divs[chain[-1]]
            chain = sorted(chain[chain.index(next_element):])
            return chain[0], len(chain)

    max_len, result = 0,0
    for i in range(4, limit+1):
        if not stop_list[i]:
            number, current_chain_len = chain_lenght(i)
            if current_chain_len > max_len:
                max_len,result = current_chain_len, number
    return result

print(p95(1000000))

print( "Time:", time() - start, "Sec.")
