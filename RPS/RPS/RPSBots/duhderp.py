from random import randint

beat = {'R':'P', 'P':'S', 'S':'R'}
if input in beat.keys():
    opmoves.append(input)
    mymoves.append(mymoves[-1] if randint(0, 1) else opmoves[-1])
else:
    opmoves = []
    mymoves = [beat.keys()[randint(0, 2)]]

output = mymoves[-1]