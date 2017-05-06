from random import randint

beat = {'R':'P', 'P':'S', 'S':'R'}
if input in beat.keys():
    mymoves.append(beat[beat[mymoves[randint(0, len(mymoves)-1)]]])
else:
    mymoves = [beat.keys()[randint(0, 2)]]

output = mymoves[-1]