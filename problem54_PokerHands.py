#https://projecteuler.net/problem=54
from time import time
start = time()
f = open('files/p054_poker.txt', 'r')
hands_list = map(lambda el:el.strip(), list(f))

combinations = ['value Card', 'One Pair', 'Two Pairs', 'Three of a Kind',\
    'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']

def transform(hand:str):
    h = hand.replace('T','10').replace('J','11').replace('Q','12').\
            replace('K','13').replace('A','14').split()
    return list(sorted(map(lambda el:[int(el[:-1]), el[-1]], h),\
                key=lambda x:x[0], reverse=True))

def check_hand(player:object):
    hand = player['hand']
    its_flush = False
    its_straiht = False
    ranks = [el[0] for el in hand]
    ranks_set = set(ranks)
    suits_set = set()
    for card in hand:
        suits_set.add(card[1])
    if len(suits_set) == 1: its_flush = True
    if list(map(lambda el:el-ranks[-1], ranks)) == list(range(5))[::-1]:
        its_straiht = True
    if its_straiht and its_flush:
        return {'combination' : 'Straight Flush', 'value' : ranks[0]}
    elif len(ranks_set) == 2:
        for rank in ranks_set:
            if ranks.count(rank) == 4:
                return {'combination' : 'Four of a Kind', 'value' : rank}
            elif ranks.count(rank) == 3:
                return {'combination' : 'Full House', 'value' : rank}
    elif its_flush:
        return {'combination' : 'Flush', 'value' : ranks[0]}
    elif its_straiht:
        return {'combination' : 'Straight', 'value' : ranks[0]}
    elif len(ranks_set) == 3:
        pairs = []
        for rank in ranks_set:
            if ranks.count(rank) == 3:
                return {'combination' : 'Three of a Kind', 'value' : rank}
            elif ranks.count(rank) == 2:
                pairs.append(rank)
        return {
        'combination' : 'Two Pairs',
        'value' : sorted(pairs, reverse=True)[0] * 100 + sorted(pairs, reverse=True)[1]
        }
    elif len(ranks_set) == 4:
        for rank in ranks_set:
            if ranks.count(rank) == 2:
                return {'combination' : 'One Pair', 'value' : rank}
    else:
        return {'combination' : 'value Card', 'value' : ranks[0]}

def winner(table:str):
    p1,p2 = {'number' : 1},{'number' : 2}
    p1['hand'], p2['hand'] = transform(table[:14]), transform(table[15:])
    p1_combo = check_hand(p1)
    p2_combo = check_hand(p2)
    if p1_combo['combination'] != p2_combo['combination']:
        if combinations.index(p1_combo['combination']) > \
            combinations.index(p2_combo['combination']):
            return 1
        else:
            return 2
    elif p1_combo['value'] != p2_combo['value']:
        if p1_combo['value'] > p2_combo['value']:
            return 1
        else:
            return 2
    else:
        for i in range(5):
            if p1['hand'][i][0]>p2['hand'][i][0]:
                return 1
            elif p1['hand'][i][0]<p2['hand'][i][0]:
                return 2

def p_54():
    count = 0
    for hand in hands_list:
        if winner(hand) == 1:
            count += 1
    return count

print(p_54())
print( "Time:", time() - start, "Sec.")
