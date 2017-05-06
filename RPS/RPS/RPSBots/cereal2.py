# See http://overview.cc/RockPaperScissors for more information about rock, paper, scissors

if input == '':
    import random
    import collections
    rps = ['R', 'P', 'S']
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
    beatboth = {'RR': 'P', 'PP': 'S', 'SS': 'R', 'PR': 'P', 'RS': 'R', 'SP': 'S','RP': 'P', 'SR': 'R', 'PS': 'S',}
    hist = ""
    patterns = collections.defaultdict(lambda: 1)
    output = random.choice(rps)
    rnd = 0
    lastplayed = dict.fromkeys(['R', 'P', 'S'], 0)
    found = 0
    foundscore = 0
else:
    rnd += 1
    for i in range(1, min(1+len(hist)/2,5)):
        patterns[hist[-i*2:]+input] += 1
    hist += output+input

    probs = [1, 1, 1]
    for i in range(1, min(1+len(hist)/2,5)):
        probs = [probs[0]*patterns[hist[-i*2:]+'R'], probs[1]*patterns[hist[-i*2:]+'P'], probs[2]*patterns[hist[-i*2:]+'S']]
    s = sum(probs)
    ma = max(probs)
    mi = min(probs)
    if s > 10 and 100 * ma / s > 90:
        found += 1
        output = beat[rps[probs.index(ma)]]
    elif s > 10 and mi * 100/s < 10 and s > 1:
        found += 1
        guess = rps[:]
        del guess[probs.index(mi)]
        output = beatboth["".join(guess)]
    else:
        lastplayed[input] = rnd 
        m = min(lastplayed.values())
        candidates = [k for k in lastplayed if lastplayed[k] != m]
        if rnd-m > 7:
            output = beat[random.choice(candidates)]
        else:
            output = random.choice(rps)