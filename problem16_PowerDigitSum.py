#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?

def power_digit_sum(power):
    return sum(int(el) for el in list(str(2 ** power)))

print(power_digit_sum(1000))
