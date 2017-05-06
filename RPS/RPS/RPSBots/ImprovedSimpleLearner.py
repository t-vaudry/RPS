import random

def beats( a ):
    if a == 'R':
        return 'P'
    if a == 'P':
        return 'S'
    if a == 'S':
        return 'R'

def record( a ):
    records[a] += 1

choices = list(['R','P','S'])


if input == '':
    prev = None
    turn = 0
    output = random.choice(choices)
    records = dict()
    records['R'] = 0
    records['P'] = 0
    records['S'] = 0
    
else:
    turn += 1
    if prev != None and prev != beats( input ):
        record( input )
    elif prev != None and input == beats( prev ):
        record( input )
        record( input )
    choices.append( beats( max(records.iterkeys(), key=lambda k: records[k]) ) ) 
    output = random.choice( choices )
    prev = output