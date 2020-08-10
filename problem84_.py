#https://projecteuler.net/problem=85
from time import time
from random import randint
start = time()

def p84():
    state = {
        'position' : 0,
        'doubles' : 0
    }

    visits = [1] + [0 for _ in range(39)]

    cc_cards = [0,10] + [None] * 14
    ch_cards = [0,10,11,24,39,5,'R','R','U',-3] + [None]*6

    def cc(pos):
        current_card = cc_cards.pop(0)
        cc_cards.append(current_card)
        if current_card:
            return current_card
        else:
            return pos

    def ch(pos):
        current_card = ch_cards.pop(0)
        ch_cards.append(current_card)
        if current_card:
            if isinstance(current_card, str):
                if current_card == 'R':
                    if pos == 7:
                        return 15
                    elif pos == 22:
                        return 25
                    else:
                        return 5
                else:
                    if pos == 22:
                        return 28
                    else:
                        return 12
            else:
                if current_card > 0:
                    return current_card
                else:
                    return pos - 3
        else:
            return pos

    def move():
        position = state['position']
        cube1 = randint(1,4)
        cube2 = randint(1,4)
        if cube1 == cube2:
            state['doubles'] += 1
            if state['doubles'] == 3:
                position = 10
                visits[position] += 1
                state['doubles'] = 0
                state['position'] = position
                return None
        else:
            state['doubles'] = 0
        position = (position + cube1 + cube2) % 40

        if position in [7,22,36]:
            position = ch(position)
        elif position in [2,17,33]:
            position = cc(position)
        elif position == 30:
            position = 10

        visits[position] += 1
        state['position'] = position
        return None

    for _ in range(1000000):
        move()
    enum = list(enumerate(visits))
    enum.sort(key=lambda x:x[1], reverse=True)
    result = ''
    for j in range(3):
        result += '{0:0>2}'.format(enum[j][0])
    return result

print(p84())
print( "Time:", time() - start, "Sec.")
