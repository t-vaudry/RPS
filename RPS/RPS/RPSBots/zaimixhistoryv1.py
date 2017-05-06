# looks at my_hands highest order matching, and then mixes all possible next moves
# based on if that old next move won or tied or lost

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections

    R, P, S = 0, 1, -1
    RPS = [R, P, S]
    TIE, WIN, LOSE = R, P, S
    PAYOFFS = [TIE, WIN, LOSE]
    inverted = [TIE, LOSE, WIN]
    to_num = {'R':R, 'P':P, 'S':S}
    to_str = ['R', 'P', 'S']
    subh = [[TIE, LOSE, WIN], [WIN, TIE, LOSE], [LOSE, WIN, TIE]]
    addh = [[R, P, S], [P, S, R], [S, R, P]]
    ties, beats, loses = addh[TIE], addh[WIN], addh[LOSE]
    POWER3 = [3 ** n for n in xrange(10)]
    ORDER = 7
    
    def hash_seq(seq, imap=itertools.imap, mul=operator.mul):
        return sum(imap(mul, seq, POWER3)) + 3 ** len(seq)
    
    def empty_vec(n):
        return [0.0] * n

    def uniform_vec(n):
        return [1.0 / n] * n
    
    def mix_scores(u, v, d):
        e = 1.0 - d
        for i in xrange(len(u)):
            u[i] = u[i] * d + v[i] * e
    
    def predictability(u, sqrt=math.sqrt):
        uniform = 1.0 / len(u)
        acc = 0.0
        for x in u:
            acc += (x - uniform) ** 2
        return sqrt(acc)

    def normalize(u):
        factor = 1.0 / sum(u)
        for i in xrange(len(u)):
            u[i] *= factor

    def pick_weighted(v):
        u = random.random()
        acc = 0.0
        for i, p in enumerate(v):
            acc += p
            if u <= acc:
                return (i, p)
    
    # mixes multiple strategies
    class Mixer(object):
        def __init__(self, decay, dropswitch, *bots):
            self.bots = bots
            self.bot_num = len(self.bots)
            self.decay = decay
            self.dropswitch = dropswitch
            self.next_hands = [None] * self.bot_num
            self.scores = [None] * self.bot_num
      
        def update(self):
            # update scores
            op_last_hand = op_hands[-1]
            for i in xrange(self.bot_num):
                last_hand = self.next_hands[i]
                if last_hand is None:
                    continue
                payoff = [last_hand[ties[op_last_hand]], last_hand[beats[op_last_hand]], last_hand[loses[op_last_hand]]]
                if payoff[LOSE] > payoff[WIN] and self.dropswitch:
                    self.scores[i] = None
                else:
                    curr_score = self.scores[i]
                    if curr_score is None:
                        self.scores[i] = payoff
                    else:
                        mix_scores(curr_score, payoff, self.decay)
         
            # compute next hand
            next_hand = empty_vec(3)
            for i in xrange(self.bot_num):
                bot_next_hand = self.bots[i].next_hand
                self.next_hands[i] = bot_next_hand
                if bot_next_hand is None:
                    continue
                curr_score = self.scores[i]
                if curr_score is None:
                    continue
                nonrandomness = predictability(curr_score)
                # nonrandomness = 1.0
                for s in PAYOFFS:
                    pscore = curr_score[s] * nonrandomness
                    offset = addh[LOSE][s]
                    for h in RPS:
                        next_hand[h] += bot_next_hand[addh[offset][h]] * pscore
            if sum(next_hand) <= 0.1:
                self.next_hand = uniform_vec(3)
            else:
                normalize(next_hand)
                self.next_hand = next_hand
    
    class HistoryMatch(object):
        def __init__(self, hands):
            self.hands = hands
            self.counts = [None for x in xrange(3**(ORDER + 1))]
            # self.counts = collections.defaultdict(lambda:None)
        
        def update(self):
            hands_len = len(self.hands)
            for order in xrange(min(ORDER, hands_len - 1)):
                index = hash_seq(self.hands[-order-2:-1])
                # index = tuple(self.hands[-order-2:-1])
                self.counts[index] = (hands_len - 1)
            self.matched_index = None
            for order in xrange(min(ORDER, hands_len) - 1, -1, -1):
                index = hash_seq(self.hands[-order-1:])
                # index = tuple(self.hands[-order-1:])
                found = self.counts[index]
                if found is not None and found > hands_len - CUTOFF:
                    self.matched_index = found
                    break
    
    class HistoryMatchBot(object):
        def __init__(self, history_matcher, ref_list, diffs):
            self.history_matcher = history_matcher
            self.ref_list = ref_list
            self.diffs = diffs
        
        def update(self):
            matched_index = self.history_matcher.matched_index
            if matched_index is None:
                self.next_hand = None
                return
            nexth = self.history_matcher.hands[matched_index]
            nextp = self.ref_list[matched_index]
            offset = self.diffs[nextp]
            
            next_hand = empty_vec(3)
            next_hand[addh[offset][nexth]] = 1.0
            
            self.next_hand = next_hand
    
    CUTOFF = 1000
    
    op_hands = []
    my_hands = []
    payoffs = []
    
    op_counts = HistoryMatch(op_hands)
    my_counts = HistoryMatch(my_hands)
    
    bots = []
    for i in xrange(-1, 2):
        for j in xrange(-1, 2):
            bots.append(HistoryMatchBot(my_counts, payoffs, [0, i, addh[i][j]]))
            # bots.append(HistoryMatchBot(op_counts, payoffs, [0, i, addh[i][j]]))
    
    predictor = Mixer(0.5, False, *bots)
    
    output = to_str[random.choice(RPS)]
    
# --------------------- turn -----------------------------
else:
    my_hands.append(to_num[output])
    op_hands.append(to_num[input])
    payoffs.append(subh[my_hands[-1]][op_hands[-1]])
    
    hands_played = len(op_hands)
    
    op_counts.update()
    my_counts.update()
    
    for b in bots:
        b.update()
    
    predictor.update()
    next_hand = pick_weighted(predictor.next_hand)[0]
    
    output = to_str[next_hand]