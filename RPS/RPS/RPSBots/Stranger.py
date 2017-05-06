def init(meta):
    pass

def v1play(i, meta):
    print i
    if i == "":
        init(meta)
        return 'R'
    else:
        return i[-1]

import zlib, random
def play(i, meta):
    if i == "":
        init(meta)
        return 'R'
    else:
        opt = 'RPS'
        random.shuffle(list(opt))
        cp = [len(zlib.compress(i+j,9)) for j in opt]
        m = min(cp)
        to_play = []
        for o, s in zip(opt, cp):
            if s == m:
                to_play.append(o)
        win = {'R': 'P', 'P': 'S', 'S': 'R'}
        return win[to_play[len(i) % len(to_play)]]
        #return i[-1]

def decide(a, b):
    if a == b:
        return 0, 0
    cmb = a+b
    outs = {'RP': (0,1), 'RS': (1,0), 'PS': (0,1)}
    if cmb in outs:
        return outs[cmb]
    if cmb[::-1] in outs:
        return outs[cmb[::-1]][::-1]

meta = {}
output = play(input, meta)