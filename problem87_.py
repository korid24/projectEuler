#https://projecteuler.net/problem=87
from time import time
start = time()

def prime_generator(top_border):
    numbers = [False for _ in range(top_border+1)]
    for i in range(2,top_border+1):
        if numbers[i]:
            continue
        else:
            for n in range(2, int(top_border/i) + 1):
                numbers[i*n] = True
            yield i

def p87(limit):
    fourth_digit_of_prime = [i**4 for i in prime_generator(int(limit ** (1/4)))]
    cube_of_prime = [i**3 for i in prime_generator(int(limit ** (1/3)))]
    square_of_prime = [i**2 for i in prime_generator(int(limit ** (1/2)))]

    s = set()
    for p4 in fourth_digit_of_prime:
        for cube in cube_of_prime:
            if p4 + cube > limit:
                break
            else:
                for square in square_of_prime:
                    if p4+cube+square >= limit:
                        break
                    else:
                        s.add(p4+cube+square)
    return len(s)

print(p87(50000000))


print( "Time:", time() - start, "Sec.")
