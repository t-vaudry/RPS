# uses an adaptive dfa to switch between the 6 ways of using beat last strategy

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections
    
    R, P, S = 0, 1, 2
    RPS = [R, P, S]
    T, W, L = R, P, S
    PAYOFFS = [T, W, L]
    scorep = [0, 1, -1]
    to_win = [W, T, L]
    convert = {'R':R, 'P':P, 'S':S, R:'R', P:'P', S:'S'}
    subh = [[T, L, W], [W, T, L], [L, W, T]]
    addh = [[R, P, S], [P, S, R], [S, R, P]]
    ties, beats, loses = addh[T], addh[W], addh[L]
    POWER3 = [3 ** n for n in xrange(10)]
    
    def pick_max(vec):
        maxix = 0
        accmax = vec[0]
        for i in xrange(1, len(vec)):
            if vec[i] >= accmax:
                accmax = vec[i]
                maxix = i
        return maxix
    
    def normalize(u):
        factor = 1.0 / sum(u)
        for i in xrange(len(u)):
            u[i] *= factor

    def pick_weighted(v):
        u = random.random()
        acc = 0.0
        for i, p in enumerate(v):
            acc += p
            if u < acc:
                return (i, p)
    
    class LastBot(object):
        def __init__(self, op_moves, offset):
            self.op_moves = op_moves
            self.offset = offset
        
        def update(self):
            self.next_hand = addh[self.offset][self.op_moves[-1]]
    
    op_hands = []
    my_hands = []
    payoffs = []
    op_payoffs = []
    
    output = convert[random.choice(RPS)]
# --------------------- turn -----------------------------
else:
    last_input, last_output = convert[input], convert[output]
    my_hands.append(last_output)
    op_hands.append(last_input)
    payoffs.append(subh[last_output][last_input])
    op_payoffs.append(subh[last_input][last_output])
    hands_played = len(op_hands)
    
    # bot initialization after first turn
    if hands_played == 1:
        bots = [
            LastBot(op_hands, W),
            LastBot(my_hands, L),
            LastBot(op_hands, T),
            LastBot(my_hands, W),
            LastBot(op_hands, L),
            LastBot(my_hands, T)]
        transitions = [
            [[0,1,0,0,0,0], [1,0,0,0,0,0], [0,0,1,0,0,0]],
            [[0,0,1,0,0,0], [0,1,0,0,0,0], [0,0,0,1,0,0]],
            [[0,0,0,1,0,0], [0,0,1,0,0,0], [0,0,0,0,1,0]],
            [[0,0,0,0,1,0], [0,0,0,1,0,0], [0,0,0,0,0,1]],
            [[0,0,0,0,0,1], [0,0,0,0,1,0], [1,0,0,0,0,0]],
            [[1,0,0,0,0,0], [0,0,0,0,0,1], [0,1,0,0,0,0]]]
        mode = 1
        for b in bots:
            b.update()
        next_hand = bots[mode].next_hand
    else:
        last_transition = transitions[mode][payoffs[-2]]
        for i in xrange(6):
            if bots[i].next_hand == beats[last_input]:
                last_transition[i] += 1
        for b in bots:
            b.update()
        
        nextstatep = transitions[mode][payoffs[-1]][:]
        normalize(nextstatep)
        # mode = pick_max(transitions[mode][payoffs[-1]])
        mode = pick_weighted(nextstatep)[0]
        next_hand = bots[mode].next_hand
    
    output = convert[next_hand]
    
    # if hands_played == 999:
        # print transitions