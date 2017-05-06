"""
Using compression to predict the opponents most likely next move.

The most likely move is assumed to be the one that with the least
complexity (least randomness) and therefore the one that has the
smallest compression size when added to the string representation
of previous moves.

bmh July 2012 <benjamin.haley@gmail.com>
"""

from zlib import compress
from random import shuffle, choice, random

moves = ['R', 'P', 'S']

comebacks = {
    ('R',): ('P',),
    ('P',): ('S',),
    ('S',): ('R',),
    ('P', 'R'): ('P',),
    ('P', 'S'): ('S',),
    ('R', 'S'): ('R',),
    ('P', 'R', 'S'): ('P', 'R', 'S'),
}


def complexity(string):
    """ What is the compressed size of a string?
    (larger is more complex)"""
    return len(compress(string, 9))

def expected(history):
    """The most likely next move of the opponent"""
    exps = [(complexity(history + m), m) for m in moves]
    patients = 2
    res = tuple(sorted([e[1] for e in exps if e[0] <= min(exps)[0] + patients]))
    return res

def player(history):
    return choice(comebacks[expected(history)])

#"""
# to compare with existing code at
# http://www.rpscontest.com/submit

if input == "":
    history = ''
else:
    history += input

output = player(history)
history += output