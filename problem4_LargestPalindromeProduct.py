#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def largestPalindrome(digitCount):
    for i in range(10 ** (digitCount * 2))[::-1]:
        if isPalindrome(i):
            for j in range(1, 10 ** digitCount)[::-1]:
                if i % j == 0 and 10 ** (digitCount-1) < i / j < 10 ** digitCount:
                    return (i, j, int(i / j))




print(largestPalindrome(3))
