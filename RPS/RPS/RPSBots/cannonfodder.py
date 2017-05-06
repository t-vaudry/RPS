import random

possible_moves = ['R', 'P', 'S']

def player(my, opp):
    return detect_pattern(opp) or \
           detect_local_skew(opp) or \
           random.choice(possible_moves)

def beat_move(move):
    return possible_moves[(possible_moves.index(move) + 1) % 3]
           
def detect_pattern(moves, frame=50, maxlen=15):
    if len(moves) < frame:
        return False
    moves = moves[-frame:]
    for i in range(1, maxlen):
        if all(moves[j] == moves[j - i] for j in range(i, frame)):
            return beat_move(moves[-i])
    return False

def detect_local_skew(moves):
    if len(moves) < 100:
        return False
    moves = moves[-100:]
    last  = moves[-1]
    nexts = [moves[i+1] for i, m in enumerate(moves[:-1]) if m == last]
    # just enough to do some inference
    if len(nexts) > 15:
        expected_prob = len(nexts) / 3.0
        skew = sum([abs(expected_prob - nexts.count(move)) for move in possible_moves])
        # 10% false positives
        if skew > 10:
            return beat_move(random.choice(nexts))


if input == "":
    my  = []
    opp = []
else:
    opp.append(input)
    
output = player(my, opp)
my.append(output)