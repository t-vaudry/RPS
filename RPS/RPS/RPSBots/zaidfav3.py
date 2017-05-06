# uses a higher order markov chain to transition between the 6 ways of
# using the beat last strategy

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
    
    class MarkovN(object):
        def __init__(self, order, op_moves, state_history, bot_list):
            self.order = order
            self.state_history = state_history
            self.op_moves = op_moves
            self.bot_list = bot_list
            self.dict = collections.defaultdict(lambda:[0,0,0,0,0,0])
        
        def update(self):
            # last turn's state
            last_state = self.state_history[-1]
            
            # op's last move
            last_op_move = self.op_moves[-1]
            
            # the highest order that can be updated
            highest_prev_order = min(len(self.state_history) - 1, self.order)
            
            # update the transitions for the bots that won last turn
            for bot_index, bot in enumerate(self.bot_list):
                if bot.next_hand == beats[last_op_move]:
                    # up to and including highest_prev_order
                    for order in xrange(highest_prev_order + 1):
                        # up to second last one
                        upper_bound = len(self.state_history) - 1
                        lower_bound = upper_bound - order
                        index = tuple(self.state_history[lower_bound:upper_bound]);
                        
                        # update last time's info
                        self.dict[index][bot_index] += 1
            
            # now find highest order that's not all 0
            highest_curr_order = min(len(self.state_history), self.order)
            for order in xrange(highest_curr_order, -1, -1):
                lower_bound = len(self.state_history) - order
                index = tuple(self.state_history[lower_bound:])
                counts = self.dict[index]
                if sum(counts) > 0:
                    self.counts = counts
                    break
                
    
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
    
    
    bots = [
        LastBot(op_hands, W),
        LastBot(my_hands, L),
        LastBot(op_hands, T),
        LastBot(my_hands, W),
        LastBot(op_hands, L),
        LastBot(my_hands, T)]
    mode = 0
    
    states = []
    
    markov = MarkovN(6, op_hands, states, bots)
# --------------------- turn -----------------------------
else:
    last_input, last_output = convert[input], convert[output]
    my_hands.append(last_output)
    op_hands.append(last_input)
    payoffs.append(subh[last_output][last_input])
    op_payoffs.append(subh[last_input][last_output])
    hands_played = len(op_hands)
    
    states.append(mode)
    
    if hands_played > 1:
        markov.update()
        
        for b in bots:
            b.update()
        
        nextstatep = markov.counts[:]
        normalize(nextstatep)
        mode = pick_weighted(nextstatep)[0]
        next_hand = bots[mode].next_hand
    else:
        for b in bots:
            b.update()
        next_hand = bots[mode].next_hand
    
    output = convert[next_hand]
    
    # output = convert[random.choice(RPS)]
    
    # if hands_played == 999:
    # if hands_played < 5:
        # print markov.dict
        # print '\
'.join(str(lst) for lst in transitions)