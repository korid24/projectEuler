#https://projecteuler.net/problem=19

day_in_month = []
for i in range(1,5):
    if i == 4:
        day_in_month += [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        day_in_month += [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_in_month *= 25
day_in_month = day_in_month[:-12]

def countingSundays():
    day_pass = 1
    count = 0
    curent_month = 0
    while day_pass < sum(day_in_month):
        day_pass += day_in_month[curent_month]
        curent_month += 1
        if day_pass % 7 == 0:
            count += 1
    return count

print(countingSundays())
