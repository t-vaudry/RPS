from random import randint

beat = {'R':'P', 'P':'S', 'S':'R'}
if input in beat.keys():
    opmoves.append(input)
    mymoves.append(beat[opmoves[randint(0, len(opmoves)-1)]] if randint(0, 1) else beat[beat[mymoves[randint(0, len(mymoves)-1)]]])
else:
    opmoves = []
    mymoves = [beat.keys()[randint(0, 2)]]

output = mymoves[-1]