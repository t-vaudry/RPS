import random
import math

RVL_V3 = '''
import random
numPre = 18
numMeta = 18
if not input:
    limit = 8
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    moves = ['', '', '']
    pScore = [[3] * numPre, [3] * numPre, [3] * numPre, [3] * numPre, [3] * numPre, [3] * numPre]
    centrifuge = {'RP': 'a', 'PS': 'b', 'SR': 'c', 'PR': 'd', 'SP': 'e', 'RS': 'f', 'RR': 'g', 'PP': 'h', 'SS': 'i'}
    length = 0
    p = [random.choice("RPS")] * numPre
    m = [random.choice("RPS")] * numMeta
    mScore = [3] * numMeta
else:
    for i in range(numPre):
        pScore[0][i] = 0.8 * pScore[0][i] + ((input == p[i]) - (input == beat[beat[p[i]]])) * 3
        pScore[1][i] = 0.8 * pScore[1][i] + ((output == p[i]) - (output == beat[beat[p[i]]])) * 3
        pScore[2][i] = 0.87 * pScore[2][i] + (input == p[i]) * 3.3 - (input == beat[p[i]]) * 0.9 - (input == beat[
            beat[p[i]]]) * 3
        pScore[3][i] = 0.87 * pScore[3][i] + (output == p[i]) * 3.3 - (output == beat[p[i]]) * 0.9 - (output == beat[
            beat[p[i]]]) * 3
        pScore[4][i] = (pScore[4][i] + (input == p[i]) * 3) * (1 - (input == beat[beat[p[i]]]))
        pScore[5][i] = (pScore[5][i] + (output == p[i]) * 3) * (1 - (output == beat[beat[p[i]]]))
    for i in range(numMeta):
        mScore[i] = (mScore[i] + (input == m[i])) * (1 - (input == beat[beat[m[i]]]))
    moves[0] += centrifuge[input + output]
    moves[1] += input
    moves[2] += output
    length += 1
    for y in range(3):
        j = min([length, limit])
        while j >= 1 and not moves[y][length - j:length] in moves[y][0:length - 1]:
            j -= 1
        i = moves[y].rfind(moves[y][length - j:length], 0, length - 1)
        p[0 + 2 * y] = moves[1][j + i]
        p[1 + 2 * y] = beat[moves[2][j + i]]

    for i in range(6, 6 * 3):
        p[i] = beat[beat[p[i - 6]]]

    for i in range(0, 6, 2):
        m[i] = p[pScore[i].index(max(pScore[i]))]
        m[i + 1] = beat[p[pScore[i + 1].index(max(pScore[i + 1]))]]
    for i in range(6, 18):
        m[i] = beat[beat[m[i - 6]]]
output = beat[m[mScore.index(max(mScore))]]
if max(mScore) < 0.13 or random.randint(3, 40) > length:
    output = beat[random.choice("RPS")]
'''


rps30 = '''
import random

nwin = 0
ntie = 0
nloss = 0
iter = 0
epsilon = 0.2
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
    if score[(output, input)] == 1: nloss += 1
    elif score[(output, input)] == 0: ntie += 1
    elif score[(output, input)] == -1: nwin += 1

    reward = score[(action, input)]
    maxvalue = max(Q.get((newstate, a), 0) for a in 'RPS')
    Q[(state, action)] = Q.get((state, action), 0) + lr * (reward + 0.5 * maxvalue - Q.get((state, action), 0))
    succ = [Q.get((newstate, a), 0) for a in 'RPS']
    optimal_actions = ['RPS'[x] for x in range(len(succ)) if succ[x] == max(succ)]
    output = random.choice(optimal_actions) if random.random() > epsilon else random.choice('RPS')
'''

dllu_defensive = '''
import random
numPre = 30
numMeta = 6
if not input:
    limit = 8
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    moves = ['', '', '', '']
    pScore = [[5] * numPre, [5] * numPre, [5] * numPre, [5] * numPre, [5] * numPre, [5] * numPre]
    centrifuge = {'RP': 0, 'PS': 1, 'SR': 2, 'PR': 3, 'SP': 4, 'RS': 5, 'RR': 6, 'PP': 7, 'SS': 8}
    centripete = {'R': 0, 'P': 1, 'S': 2}
    soma = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    rps = [1, 1, 1];
    a = "RPS"
    best = [0, 0, 0];
    length = 0
    p = [random.choice("RPS")] * numPre
    m = [random.choice("RPS")] * numMeta
    mScore = [5, 2, 5, 2, 4, 2]
    dithering = 0.7
else:
    for i in range(numPre):
        pp = p[i]
        bpp = beat[pp]
        bbpp = beat[bpp]
        pScore[0][i] = 0.9 * pScore[0][i] + ((input == pp) - (input == bbpp)) * 3
        pScore[1][i] = 0.9 * pScore[1][i] + ((output == pp) - (output == bbpp)) * 3
        pScore[2][i] = 0.87 * pScore[2][i] + (input == pp) * 3.3 - (input == bpp) * 1.2 - (input == bbpp) * 2.3
        pScore[3][i] = 0.87 * pScore[3][i] + (output == pp) * 3.3 - (output == bpp) * 1.2 - (output == bbpp) * 2.3
        pScore[4][i] = (pScore[4][i] + (input == pp) * 3) * (1 - (input == bbpp))
        pScore[5][i] = (pScore[5][i] + (output == pp) * 3) * (1 - (output == bbpp))
    for i in range(numMeta):
        mScore[i] = 0.96 * (mScore[i] + (input == m[i]) - (input == beat[beat[m[i]]])) + (
                                                                                         random.random() - 0.5) * dithering
    soma[centrifuge[input + output]] += 1;
    rps[centripete[input]] += 1;
    moves[0] += str(centrifuge[input + output])
    moves[1] += input
    moves[2] += output
    length += 1
    for y in range(3):
        j = min([length, limit])
        while j >= 1 and not moves[y][length - j:length] in moves[y][0:length - 1]:
            j -= 1
        i = moves[y].rfind(moves[y][length - j:length], 0, length - 1)
        p[0 + 2 * y] = moves[1][j + i]
        p[1 + 2 * y] = beat[moves[2][j + i]]
    j = min([length, limit])
    while j >= 2 and not moves[0][length - j:length - 1] in moves[0][0:length - 2]:
        j -= 1
    i = moves[0].rfind(moves[0][length - j:length - 1], 0, length - 2)
    if j + i >= length:
        p[6] = p[7] = random.choice("RPS")
    else:
        p[6] = moves[1][j + i]
        p[7] = beat[moves[2][j + i]]

    best[0] = soma[centrifuge[output + 'R']] * rps[0] / rps[centripete[output]]
    best[1] = soma[centrifuge[output + 'P']] * rps[1] / rps[centripete[output]]
    best[2] = soma[centrifuge[output + 'S']] * rps[2] / rps[centripete[output]]
    p[8] = p[9] = a[best.index(max(best))]

    for i in range(10, numPre):
        p[i] = beat[beat[p[i - 10]]]

    for i in range(0, numMeta, 2):
        m[i] = p[pScore[i].index(max(pScore[i]))]
        m[i + 1] = beat[p[pScore[i + 1].index(max(pScore[i + 1]))]]
output = beat[m[mScore.index(max(mScore))]]
if max(mScore) < 3 + random.random() or random.randint(3, 40) > length:
    output = beat[random.choice("RPS")]
'''

if not input:
    arm1 = compile(RVL_V3, '<string>', 'exec')
    arm2 = compile(rps30, '<string>', 'exec')
    arm3 = compile(dllu_defensive, '<string>', 'exec')
    scope1 = {'input': input}
    scope2 = {'input': input}
    scope3 = {'input': input}
    score = {
        ('R', 'R'): 0, ('R', 'P'): -1, ('R', 'S'): 1,
        ('P', 'R'): 1, ('P', 'P'): 0, ('P', 'S'): -1,
        ('S', 'R'): -1, ('S', 'P'): 1, ('S', 'S'): 0
    }
    alpha = 0.4
    beta = 0.98
    exec arm1 in scope1
    a1 = scope1['output']
    exec arm2 in scope2
    a2 = scope2['output']
    exec arm3 in scope3
    a3 = scope3['output']
    pi = [0] * 3
    rbar = 0
    output = random.choice([a1, a2, a3])
    choice = [a1, a2, a3].index(output)
else:
    rew = score[(output, input)]
    pi[choice] = pi[choice] + beta * (rew - rbar)
    rbar = (1 - alpha) * rbar + alpha * rbar
    scope1['input'] = input
    scope1['output'] = output
    scope2['input'] = input
    scope2['output'] = output
    scope3['input'] = input
    scope3['output'] = output
    exec arm1 in scope1
    a1 = scope1['output']
    exec arm2 in scope2
    a2 = scope2['output']
    exec arm3 in scope3
    a3 = scope3['output']
    maxvalue = max(pi)
    Z = sum(math.exp(x - maxvalue) for x in pi)
    p = [math.exp(x - maxvalue) / Z for x in pi]
    u = random.random()
    if u < p[0]:
        choice = 0
    elif p[0] <= u < p[0] + p[1]:
        choice = 1
    elif u >= p[1] + p[0]:
        choice = 2

    output = [a1, a2, a3][choice]