import random

DEPTH = 2

def likelihood(table, last_moves, move) :
    res = table.get(tuple(last_moves), [])
    if res :
        will_win = [r for r in res if to_win[r] == move]
        return float(len(will_win))/float(len(res))
    else :
        return 0.2

def get_best_move(table, last_moves) :
    l_R = likelihood(table, last_moves, "R")
    l_P = likelihood(table, last_moves, "P")
    l_S = likelihood(table, last_moves, "S")
    res = [("R", l_R), ("P", l_P), ("S", l_S)]
    res.sort(key=lambda x : x[1])
    return res[-1][0]

if not input :
    moves = ["R", "P", "S"]
    to_win = {"R":"P", "P":"S", "S":"R"}
    to_lose = {"R":"S", "P":"R", "S":"P"}
    curr_history = []
    for i in xrange(DEPTH) :
        curr_history.append((random.choice(moves), random.choice(moves))) # just loading it with something non-important
    table = dict()
    last_move = random.choice(moves)
    output = last_move
else :
    key = tuple(curr_history)
    if key in table :
        table[key].append(input)
    else :
        table[key] = [input]
    output = get_best_move(table, curr_history)
    curr_history.append((last_move, input))
    last_move = output
    curr_history.pop(0)