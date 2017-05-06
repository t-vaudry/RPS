import random

beats = {'R': 'S',
         'P': 'R',
         'S': 'P'}

loses = {'R': 'P',
         'P': 'R',
         'S': 'R'}

def gen_strat_meta_one(strat):
    def strat_meta_one(hist):
        return beats[strat(hist)]
    return strat_meta_one

def gen_strat_meta_two(strat):
    def strat_meta_two(hist):
        return beats[beats[strat(hist)]]
    return strat_meta_two

def all_level(strat):
    return [strat, gen_strat_meta_one(strat), gen_strat_meta_two(strat)]

def strat_rand(hist):
    return random.choice(["R", "P", "S"])

def strat_const(hist):
    return 'R'

def strat_freq(hist):
    r = p = s = 0
    for (_, m) in hist:
        if m == 'P':
            p += 1 
        elif m == 'R':
            r += 1
        else:
            s += 1
    if r > p and r > s:
        return 'P'
    elif p > s:
        return 'S'
    else:
        return 'R' 

def strat_beat_last(hist):
    if len(hist) < 1:
        return strat_rand(hist)
    return loses[hist[-1][1]]

all_strat = [strat_rand]
            #strat_freq,
            #strat_beat_last]

def count_wins(strat, hist):
    wins = 0
    for size in xrange(0, len(hist)):
        short_hist = hist[:size]
        chose = strat(short_hist)
        opp_chose = hist[size][1]
        if beats[opp_chose] == chose:
            wins += 1
    return wins

def most_winning(hist):
    best = all_strat[0]
    count = count_wins(all_strat[0], hist)
    for strat in all_strat[1:]:
        c = count_wins(strat, hist)
        if c > count:
            count = c
            best = strat
    return best

def reply(hist):
    strat = most_winning(hist)
    return strat(hist)

if input == "":
    ghist = []
    output = pending = strat_rand([])
else:
    ghist.append((pending, input))
    output = pending = beats[strat_beat_last(ghist)]