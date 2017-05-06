# mixes the strategies that try to play in the opponent's shoes

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections
    
    R, P, S = 0, 1, 2
    RPS = [R, P, S]
    T, W, L = R, P, S
    PAYOFFS = [T, W, L]
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
    
    # def score_counts(counts):
        # score = 0
        # for s in PAYOFFS:
            # score += counts[s] * s
        # return score
    
    # mixes multiple strategies
    class Mixer(object):
        def __init__(self, decay_function, dropswitch, *bots):
            self.bots = bots
            self.bot_num = len(self.bots)
            self.decay_function = decay_function
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
                if payoff[L] > payoff[W] and self.dropswitch:
                    self.scores[i] = None
                else:
                    if self.scores[i] is None:
                        self.scores[i] = uniform_vec(3)
                    mix_scores(self.scores[i], payoff, self.decay_function(len(op_hands)))
         
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
                    offset = addh[L][s]
                    for h in RPS:
                        next_hand[h] += bot_next_hand[addh[offset][h]] * pscore
            if sum(next_hand) <= 0.1:
                self.next_hand = pick_weighted(uniform_vec(3))[0]
            else:
                normalize(next_hand)
                self.next_hand = pick_weighted(next_hand)[0]
    
    class History(object):
        def __init__(self, order, offset, *handss):
            self.order = order
            self.offset = offset
            self.handss = handss
            self.handss_num = len(handss)
            self.all = []
            self.counts = collections.defaultdict(list)
        
        def update(self):
            # update the all list
            last_hands = [self.handss[i][-1] for i in xrange(self.handss_num)]
            code = 0
            for i in xrange(self.handss_num):
                code += last_hands[i] * POWER3[i]
            self.all.append(code)
            hands_len = len(self.all)
            
            # update for the previous hand
            for order in xrange(min(self.order, hands_len - 1)):
                index = tuple(self.all[-order-2:-1])
                self.counts[index].append(code)
            
            # setup the next one and predict
            prediction = [0] * 3
            for order in xrange(min(self.order, hands_len)):
                index = tuple(self.all[-order-1:])
                past = self.counts[index]
                if past:
                    mine, ops = self.decode3(past[-1])
                    if subh[mine][ops] == W:
                        prediction[mine] = 1.0
            if sum(prediction) < 0.01:
                self.next_hand = None
            else:
                normalize(prediction)
                offsetted = [0.0] * 3
                offsetted[addh[self.offset][R]] = prediction[R]
                offsetted[addh[self.offset][P]] = prediction[P]
                offsetted[addh[self.offset][S]] = prediction[S]
                self.next_hand = offsetted
        
        def decode3(self, code):
            hands = []
            for i in xrange(self.handss_num):
                hands.append(code % 3)
                code /= 3
            return hands
    
    class ConstantBot(object):
        def __init__(self, op_moves, my_moves, offset):
            self.op_moves = op_moves
            self.my_moves = my_moves
            self.offset = offset
            next_hand_p = [0.0] * 3
            next_hand_p[addh[offset][my_moves[-1]]] = 1.0
            self.next_hand = next_hand_p
        
        def update(self):
            pass
    
    class BeatLastBot(object):
        def __init__(self, op_moves, my_moves, offset):
            self.op_moves = op_moves
            self.my_moves = my_moves
            self.offset = offset
        
        def update(self):
            next_hand_p = [0.0] * 3
            next_hand_p[addh[self.offset][self.op_moves[-1]]] = 1.0
            self.next_hand = next_hand_p
    
    op_hands = []
    my_hands = []
    payoffs = []
    
    output = convert[random.choice(RPS)]
# --------------------- turn -----------------------------
else:
    last_input, last_output = convert[input], convert[output]
    my_hands.append(last_output)
    op_hands.append(last_input)
    payoffs.append(subh[last_output][last_input])
    hands_played = len(op_hands)
    
    # bot initialization after first turn
    if hands_played == 1:
        # constantbot = ConstantBot(op_hands, my_hands, T)
        # constantbot2 = ConstantBot(my_hands, op_hands, W)
        beatlastbot = BeatLastBot(op_hands, my_hands, T)
        beatlastbot2 = BeatLastBot(my_hands, op_hands, W)
        hist = History(5, T, my_hands, op_hands)
        hist2 = History(5, W, op_hands, my_hands)
        
        mixer = Mixer(lambda x:0.9, False, beatlastbot, beatlastbot2, hist, hist2)
    
    # constantbot.update()
    # constantbot2.update()
    beatlastbot.update()
    beatlastbot2.update()
    hist.update()
    hist2.update()
    mixer.update()
    
    output = convert[mixer.next_hand]