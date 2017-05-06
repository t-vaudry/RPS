# looks for history match and the score of that last hand
# and plays a bit randomly to counter

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections
    
    R, P, S = 0, 1, 2
    RPS = [R, P, S]
    T, W, L = R, P, S
    PAYOFFS = [T, W, L]
    score_payoff = [0, 1, -1]
    to_win = [W, T, L]
    convert = {'R':R, 'P':P, 'S':S, R:'R', P:'P', S:'S'}
    subh = [[T, L, W], [W, T, L], [L, W, T]]
    addh = [[R, P, S], [P, S, R], [S, R, P]]
    ties, beats, loses = addh[T], addh[W], addh[L]
    POWER3 = [3 ** n for n in xrange(10)]
    
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
    
    def score_counts(counts):
        score = 0
        for s in PAYOFFS:
            score += counts[s] * score_payoff[s]
        return score
    
    class History(object):
        def __init__(self, order, *handss):
            self.order = order
            self.handss = handss
            self.handss_num = len(handss)
            self.all = []
            self.counts = collections.defaultdict(list)
        
        def update(self):
            # update the all list
            code = 0
            for i in xrange(self.handss_num):
                code += self.handss[i][-1] * POWER3[i]
            self.all.append(code)
            hands_len = len(self.all)
            
            # update for the previous hand
            for order in xrange(min(self.order, hands_len - 1)):
                index = tuple(self.all[-order-2:-1])
                self.counts[index].append(code)
            
            # setup the next one and predict
            prediction = None
            for order in xrange(min(self.order, hands_len)):
                index = tuple(self.all[-order-1:])
                cur_counts_order = self.counts[index]
                if len(cur_counts_order) >= 1:
                    prediction = cur_counts_order[-1]
            if prediction is not None:
                prediction = self.decode3(prediction)
            self.prediction = prediction
        
        def decode3(self, code):
            hands = []
            for i in xrange(self.handss_num):
                hands.append(code % 3)
                code /= 3
            return hands
    
    op_hands = []
    my_hands = []
    payoffs = []
    next_hand = random.choice(RPS)
    
    hist = History(7, op_hands, my_hands)
    
    output = convert[next_hand]
# --------------------- turn -----------------------------
else:
    last_input, last_output = convert[input], convert[output]
    my_hands.append(last_output)
    op_hands.append(last_input)
    payoffs.append(subh[last_output][last_input])
    hands_played = len(op_hands)
    
    hist.update()
    
    next_hand_p = hist.prediction
    if next_hand_p is not None:
        score = subh[next_hand_p[1]][next_hand_p[0]]
        if score == W:
            if random.random() < 0.7:
                next_hand = ties[next_hand_p[1]]
            else:
                next_hand = loses[next_hand_p[1]]
        elif score == T:
            if random.random() < 0.7:
                next_hand = beats[next_hand_p[1]]
            else:
                next_hand = ties[next_hand_p[1]]
        else:
            if random.random() < 0.7:
                next_hand = loses[next_hand_p[1]]
            else:
                next_hand = beats[next_hand_p[1]]
    output = convert[next_hand]