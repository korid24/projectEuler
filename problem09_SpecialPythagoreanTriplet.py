#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#a,b,c = (m ** 2 - n ** 2), (2 * m * n), (m ** 2 + n ** 2)
#m ** 2 + mn == x / 2
#m > n

def findProduct(x):
    for m in range(1,int(x ** 0.5)):
        for n in range(1,m):
            if m ** 2 + m * n == x / 2:
                a,b,c = (m ** 2 - n ** 2), (2 * m * n), (m ** 2 + n ** 2)
                return sorted((a,b,c,a*b*c))
    return False

print(findProduct(1000))
