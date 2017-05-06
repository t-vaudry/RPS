# author: matto
#
# first bot for RPS that is only supposed to beat
# the sample from http://www.rpscontest.com/submit
# that keeps track of history by counting

WINNER = {'R' : 'P', 'P' : 'S', 'S' : 'R'}

# first round
if not input:

    import random
    
    rpsce = {'R' : 0, 'P' : 0, 'S' : 0}
    rpscs = {'R' : 0, 'P' : 0, 'S' : 0}
    output = random.choice(["R","P","S"])
    rpscs[output] += 1
    
# not first round
else:

    rpsce[input] += 1
    if rpscs['R'] > rpscs['P'] and rpscs['R'] > rpscs['S']:
        output = WINNER[WINNER['R']]
    elif rpscs['P'] > rpscs['S']:
        output = WINNER[WINNER['P']]
    else:
        output = WINNER[WINNER['S']]
    rpscs[output] += 1