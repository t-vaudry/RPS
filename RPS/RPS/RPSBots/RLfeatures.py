import random

nwin = 0
ntie = 0
nloss = 0
iter = 0
epsilon = 0.2
#input = ""
#while True:
if not input:
    score = {
        ('R', 'R'): 0, ('R', 'P'): -1, ('R', 'S'): 1,
        ('P', 'R'): 1, ('P', 'P'): 0, ('P', 'S'): -1,
        ('S', 'R'): -1, ('S', 'P'): 1, ('S', 'S'): 0
    }
    Q = dict()
    lr = 0.9
    limits = [5, 15, 30]
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    urmoves = ""
    mymoves = ""
    DNAmoves = ""
    output = random.choice(['R', 'P', 'S'])
    nuclease = {'RP': 'a', 'PS': 'b', 'SR': 'c', 'PR': 'd', 'SP': 'e', 'RS': 'f', 'RR': 'g', 'PP': 'h', 'SS': 'i'}
    length = 0
    output = random.choice('RPS')
    newstate = tuple()
else:
    # History matching
    urmoves += input
    mymoves += output
    DNAmoves += nuclease[input + output]
    length += 1

    state = newstate
    newstate = []
    for z in range(1):
        limit = min([length, limits[z]])
        j = limit
        while j >= 1 and not DNAmoves[length - j:length] in DNAmoves[0:length - 1]:
            j -= 1
        if j >= 1:
            i = DNAmoves.rfind(DNAmoves[length - j:length], 0, length - 1)  # You seem to be playing based on our moves
            newstate.append(urmoves[j + i])
            newstate.append(mymoves[j + i])
        j = limit
        while j >= 1 and not urmoves[length - j:length] in urmoves[0:length - 1]:
            j -= 1
        if j >= 1:
            i = urmoves.rfind(urmoves[length - j:length], 0, length - 1)  # You seem to be playing based on your moves
            newstate.append(urmoves[j+i])
            newstate.append(mymoves[j+i])
        j = limit
        while j >= 1 and not mymoves[length - j:length] in mymoves[0:length - 1]:
            j -= 1
        if j >= 1:
            i = mymoves.rfind(mymoves[length - j:length], 0, length - 1)  # You seem to be playing based on my moves
            newstate.append(urmoves[j+i])
            newstate.append(mymoves[j+i])

    newstate = tuple(newstate)
    action = output
#        print "program gives: %s" % output
    if score[(output, input)] == 1: nloss += 1
    elif score[(output, input)] == 0: ntie += 1
    elif score[(output, input)] == -1: nwin += 1

    reward = score[(action, input)]
    maxvalue = max(Q.get((newstate, a), 0) for a in 'RPS')
    Q[(state, action)] = Q.get((state, action), 0) + lr * (reward + 0.5 * maxvalue - Q.get((state, action), 0))
    succ = [Q.get((newstate, a), 0) for a in 'RPS']
    optimal_actions = ['RPS'[x] for x in range(len(succ)) if succ[x] == max(succ)]
    output = random.choice(optimal_actions) if random.random() > epsilon else random.choice('RPS')