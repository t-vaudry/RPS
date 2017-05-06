"""
Using baysian logic and laplace smoothing to predict
the most likely next move.  Plays only conservative
moves.

bmh July 2012 <benjamin.haley@gmail.com>
"""

from random import choice

moves = 'RPS'

values = {
    'RR':  0.,
    'RP':  1.,
    'RS': -1.,
    'PR': -1.,
    'PP':  0.,
    'PS':  1.,
    'SR':  1.,
    'SP': -1.,
    'SS':  0.,
}

def get_probable_moves(history, laplace=1, lookback=6):
    odds = {'R':1./3, 'P':1./3, 'S':1./3}
    h, l = history, laplace      
    for i in range(1, lookback + 1):
        found = h.count(h[-i:])
        for m in moves:
            odds[m] *= (1.*(h.count(h[-i:] + m) + l) / (found + l))
        normalize = sum(odds.values())
        for m in moves:
            odds[m] /= normalize
    return odds

def get_move_values(probs):
    """return the value of each move, RPS, given a
    dictionary of the odds that the oponent will make
    any given move"""
    values_ = {}
    for my in moves:
        values_[my] = sum([p * values[his+my] for his, p in probs.items()])
    return values_

def player(history):
    odds = get_probable_moves(history, laplace, lookback)
    values_ = get_move_values(odds)
    if max(values_.values()) > threshold:
        print round(max(values_.values()), 2)
        return max(values_, key=values_.get)
    else:
        print '.',
        return choice(moves)

#"""
# to compare with existing code at
# http://www.rpscontest.com/submit
laplace = 5.
threshold = 0.35
lookback = 2

if input == '':
    history = ''
else:
    history += input

output = player(history)
history += output

def test():
    assert get_move_values({'R':1., 'P':0., 'S':0.})=={'P': 1.0, 'S': -1.0, 'R': 0.0}  
    assert get_move_values({'R':0.5, 'P':0.5, 'S':0.}) == {'P': 0.5, 'S': 0.0, 'R': -0.5}
    assert get_probable_moves('R', 0, 0)['R'] == 1./3
    assert get_probable_moves('RR', 0, 1)['R'] == 1.
    assert get_probable_moves('RR', 1, 1)['R'] == 2. / 4
    assert get_probable_moves('RP'*5)['R'] > get_probable_moves('RP'*5)['S']
    assert player('RRRRRR') == 'P'

#test()