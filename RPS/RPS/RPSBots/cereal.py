# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

if input == '':
    import random
    rps = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
    beatboth = {'RR': 'P', 'PP': 'S', 'SS': 'R', 'PR': 'P', 'RS': 'R', 'SP': 'S','RP': 'P', 'SR': 'R', 'PS': 'S',}
    opphist = ""
    output = random.choice(rps)
    rnd = 0
    lastplayed = dict.fromkeys(['R', 'P', 'S'], 0)
    foundscore = 0
    foundtotal = 0
    found = False
else:
    if found:
        foundscore += score[output+input]
    found = False
    rnd += 1
    lastplayed[input] = rnd 
    m = min(lastplayed.values())
    candidates = [k for k in lastplayed if lastplayed[k] != m]
    if rnd-m > 7:
        found = True
        foundtotal += 1
        output = beat[random.choice(candidates)]
    else:
        output = random.choice(rps)