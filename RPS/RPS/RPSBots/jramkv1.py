import random
from operator import itemgetter

if input == '':
    moves = list('RPS')
    movebeaters = {'R':'P', 'P':'S', 'S':'R'}
    output = 'rand'
    myhist = []
    opphist = []
    movedata = {}
    rounds = 0
    #print movedata
else:
    rounds += 1
    opphist.append(input)

    assert len(opphist) == len(myhist), 'unequal hist length, round {}'.format(rounds)

    if rounds == 1:
        output = 'rand'
    else:
        k2 = opphist[-2]+myhist[-2]
        if k2 not in movedata:
            movedata[k2] = {}
        movedata[k2][opphist[-1]] = movedata[k2].get(opphist[-1],0) + 1

        #if rounds == 100:
        #    print movedata

        k1 = opphist[-1]+myhist[-1]

        foo = movedata.get(k1,{})

        if len(foo) == 0:
            output = 'rand'
        else:
            #f = [reversed(x) for x in foo.iteritems()]
            #f.sort()
            f = sorted(foo.items(), key=itemgetter(-1))
            f = [x for x,y in f]
            expectedmove = f[-1]
            output = movebeaters[expectedmove]
        
if output == 'rand':
    output = random.choice(moves)

assert output=='R' or output=='P' or output=='S', 'bad output'


myhist = myhist[-5:]
opphist = opphist[-5:]

myhist.append(output)