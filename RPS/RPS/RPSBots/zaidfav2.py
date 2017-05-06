# higher order context switching between the strategies

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections
    
    STATES = ['0','1','2','3','4','5']
    R, P, S = 'R', 'P', 'S'
    RPS = [R, P, S]
    T, W, L = R, P, S
    PAYOFFS = [T, W, L]
    scorep = {T:0, W:1, L:-1}
    # to_win = [W, T, L]
    subh = {R:{R:T, P:L, S:W}, P:{R:W, P:T, S:L}, S:{R:L, P:W, S:T}}
    addh = {R:{R:R, P:P, S:S}, P:{R:P, P:S, S:R}, S:{R:S, P:R, S:P}}
    ties, beats, loses = addh[T], addh[W], addh[L]
    
    def score_hand(h, vec):
        score = 0
        for k, v in vec.iteritems():
            score += scorep[subh[h][k]] * v
        return score
    
    def regulate(vec):
        m = max(min(vec.itervalues()), 0)
        for k in vec.iterkeys():
            vec[k] -= m
    
    def pick_max(vec):
        maxix = 0
        accmax = vec[0]
        for i in xrange(1, len(vec)):
            if vec[i] >= accmax:
                accmax = vec[i]
                maxix = i
        return maxix
    
    def normalize(u):
        factor = 1.0 / sum(u.itervalues())
        for k in u.iterkeys():
            u[k] *= factor

    def pick_weighted(v):
        u = random.random()
        acc = 0.0
        for k, p in v.iteritems():
            acc += p
            if u < acc:
                return (k, p)
    
    class History(object):
        def __init__(self, order, defaultval):
            self.order = order
            self.all = []
            self.counts = collections.defaultdict(defaultval)
        
        def getprev(self, *handss):
            hands_len = len(handss[0])
            vals = []
            for order in xrange(min(self.order, hands_len - 1)):
                index = ''
                for hands in handss:
                    index += hands[-order-1:-1]
                vals.append(self.counts[index])
            return vals
        
        def getcurr(self, *handss):
            hands_len = len(handss[0])
            vals = []
            for order in xrange(min(self.order, hands_len)):
                index = ''
                for hands in handss:
                    index += hands[-order:] if order > 0 else ''
                vals.append(self.counts[index])
            return vals
    
    class HistoryBot(object):
        def __init__(self):
            self.hist = History(8, lambda:{R:1,P:1,S:1})
            
        def update(self, op_moves, my_moves):
            # update last contexts
            prevs = self.hist.getprev(op_moves, my_moves)
            cur_opmove = op_moves[-1]
            cur_mymove = my_moves[-1]
            for c in prevs:
                c[cur_opmove] += 1
            
            # use counts to predict next one
            currs = self.hist.getcurr(op_moves, my_moves)
            for i in xrange(len(currs) - 1, -1, -1):
                ps = currs[i].copy()
                if sum(ps.itervalues()) > 5:
                    normalize(ps)
                    pnext = pick_weighted(ps)[0]
                    self.next_hand = beats[pnext]
                    return
            self.next_hand = random.choice(RPS)
    
    class SwitchBot(object):
        def __init__(self):
            self.hist = History(6, lambda:{'0':0,'1':0,'2':0,'3':0,'4':0,'5':0})
            self.states = '00'
            self.bots = {
                '0':LastBot(W), '1':LastBot(L), '2':LastBot(T),
                '3':LastBot(W), '4':LastBot(L), '5':LastBot(T)}
            
        def update(self, op_moves, my_moves, payoffs):
            # update last contexts
            prevs = self.hist.getprev(self.states)
            beatlast_opmove = beats[op_moves[-1]]
            loseslast_opmove = beats[beatlast_opmove]
            # last_state = self.states[-1]
            
            for k, b in self.bots.iteritems():
                if b.next_hand == beatlast_opmove:
                    for c in prevs:
                        c[k] += 1
                # elif b.next_hand == loseslast_opmove:
                    # for c in prevs:
                        # c[k] -= min(1, c[k])
            # print prevs
            # update the bots
            self.bots['0'].update(op_moves)
            self.bots['1'].update(my_moves)
            self.bots['2'].update(op_moves)
            self.bots['3'].update(my_moves)
            self.bots['4'].update(op_moves)
            self.bots['5'].update(my_moves)
            
            # use counts to predict next one
            currs = self.hist.getcurr(self.states)
            nextstate = random.choice(STATES)
            for i in xrange(len(currs) - 1, -1, -1):
                ps = currs[i].copy()
                if sum(ps.itervalues()) > i:
                    normalize(ps)
                    nextstate = pick_weighted(ps)[0]
                    break
            self.states += nextstate
            self.next_hand = self.bots[nextstate].next_hand
    
    class LastBot(object):
        def __init__(self, offset):
            self.offset = offset
        
        def update(self, op_moves):
            self.next_hand = addh[self.offset][op_moves[-1]]
    
    class ConstantBot(object):
        def __init__(self, my_moves, offset):
            self.next_hand = addh[offset][my_moves[-1]]
        
        def update(self):
            pass
    
    op_hands = ''
    my_hands = ''
    payoffs = ''
    op_payoffs = ''
    
    output = random.choice(RPS)
# --------------------- turn -----------------------------
else:
    my_hands += (output)
    op_hands += (input)
    payoffs += (subh[output][input])
    # op_payoffs += (subh[input][output])
    hands_played = len(op_hands)
    
    # bot initialization after first turn
    if hands_played == 1:
        bot = SwitchBot()
        # bot = HistoryBot()
        
        # update the bots
        bot.bots['0'].update(op_hands)
        bot.bots['1'].update(my_hands)
        bot.bots['2'].update(op_hands)
        bot.bots['3'].update(my_hands)
        bot.bots['4'].update(op_hands)
        bot.bots['5'].update(my_hands)
        
        # bot.update(op_hands, my_hands, payoffs)
        
        next_hand = beats[op_hands[-1]]
    else:
        bot.update(op_hands, my_hands, payoffs)
        next_hand = bot.next_hand
    
    output = next_hand
    
    # if hands_played == 999:
        # print mode_counts
        # print transitions