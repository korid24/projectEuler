#https://projecteuler.net/problem=17

dct = {
    '1' : 3,
    '2' : 3,
    '3' : 5,
    '4' : 4,
    '5' : 4,
    '6' : 3,
    '7' : 5,
    '8' : 5,
    '9' : 4,
    '10' : 3,
    '11' : 6,
    '12' : 6,
    '13' : 8,
    '14' : 8,
    '15' : 7,
    '16' : 7,
    '17' : 9,
    '18' : 8,
    '19' : 8,
    '20' : 6,
    '30' : 6,
    '40' : 5,
    '50' : 5,
    '60' : 5,
    '70' : 7,
    '80' : 6,
    '90' : 6,
    '100' : 7,
    '00' : 0,
}

def leteral_srt_len(n):
    if str(n) in list(dct.keys()):
        lenght = dct[str(n)]
    else:
        arr = [str(int(n / 10) * 10), str(n % 10)]
        lenght = dct[arr[0]] + dct[arr[1]]
    return lenght

def NLC():
    one_9 = 0
    for i in range(1, 10):
        one_9 += leteral_srt_len(i)
    one_99 = 0
    for j in range(1, 100):
        one_99 += leteral_srt_len(j)
    return one_9 * 100 + one_99 * 10 + 9 * len('hundred') + 891 * len('hundredand') + len('onethousand')





print(leteral_srt_len(21))
print(NLC())
