import zlib, random
def play(i, meta):
    if i == "":
        return random.choice('RPS')
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

if input == '':
    meta = {}
    output = play(input, meta)
    meta['outs'] = [output]
    meta['ins'] = [input]
else:
    meta['ins'] += [input]
    output = play(''.join(meta['ins']), meta)
    meta['outs'].append(output)