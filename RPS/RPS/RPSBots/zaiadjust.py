# history matching adjustor on beat last

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections

    R, P, S = 0, 1, -1
    RPS = [R, P, S]
    TIE, WIN, LOSE = R, P, S
    PAYOFFS = [TIE, WIN, LOSE]
    to_win = [WIN, TIE, LOSE]
    inverted = [TIE, LOSE, WIN]
    to_num = {'R':R, 'P':P, 'S':S}
    to_str = ['R', 'P', 'S']
    subh = [[TIE, LOSE, WIN], [WIN, TIE, LOSE], [LOSE, WIN, TIE]]
    addh = [[R, P, S], [P, S, R], [S, R, P]]
    ties, beats, loses = addh[TIE], addh[WIN], addh[LOSE]
    
    # def hash_seq(seq, imap=itertools.imap, mul=operator.mul):
        # return sum(imap(mul, seq, POWER3)) + 3 ** len(seq)
    
    # def empty_vec(n):
        # return [0.0] * n

    # def uniform_vec(n):
        # return [1.0 / n] * n
    
    # def mix_scores(u, v, d):
        # e = 1.0 - d
        # for i in xrange(len(u)):
            # u[i] = u[i] * d + v[i] * e
    
    # def predictability(u, sqrt=math.sqrt):
        # uniform = 1.0 / len(u)
        # acc = 0.0
        # for x in u:
            # acc += (x - uniform) ** 2
        # return sqrt(acc)

    # def normalize(u):
        # factor = 1.0 / sum(u)
        # for i in xrange(len(u)):
            # u[i] *= factor

    # def pick_weighted(v):
        # u = random.random()
        # acc = 0.0
        # for i, p in enumerate(v):
            # acc += p
            # if u <= acc:
                # return (i, p)
    
    # # mixes multiple strategies
    # class Mixer(object):
        # def __init__(self, decay_function, dropswitch, *bots):
            # self.bots = bots
            # self.bot_num = len(self.bots)
            # self.decay_function = decay_function
            # self.dropswitch = dropswitch
            # self.next_hands = [None] * self.bot_num
            # self.scores = [None] * self.bot_num
            # self.next_hand = bots[0].next_hand
      
        # def update(self):
            # # update scores
            # op_last_hand = op_hands[-1]
            # for i in xrange(self.bot_num):
                # last_hand = self.next_hands[i]
                # if last_hand is None:
                    # continue
                # temp = uniform_vec(3)
                # temp[last_hand] = 1.0
                # last_hand = temp
                # payoff = [last_hand[ties[op_last_hand]], last_hand[beats[op_last_hand]], last_hand[loses[op_last_hand]]]
                # if payoff[LOSE] > payoff[WIN] and self.dropswitch:
                    # self.scores[i] = None
                # else:
                    # if self.scores[i] is None:
                        # self.scores[i] = uniform_vec(3)
                    # mix_scores(self.scores[i], payoff, self.decay_function(len(op_hands)))
         
            # # compute next hand
            # next_hand = empty_vec(3)
            # for i in xrange(self.bot_num):
                # bot_next_hand = self.bots[i].next_hand
                # self.next_hands[i] = bot_next_hand
                # if bot_next_hand is None:
                    # continue
                # temp = uniform_vec(3)
                # temp[bot_next_hand] = 1.0
                # bot_next_hand = temp
                # curr_score = self.scores[i]
                # if curr_score is None:
                    # continue
                # nonrandomness = predictability(curr_score)
                # # nonrandomness = 1.0
                # for s in PAYOFFS:
                    # pscore = curr_score[s] * nonrandomness
                    # offset = addh[LOSE][s]
                    # for h in RPS:
                        # next_hand[h] += bot_next_hand[addh[offset][h]] * pscore
            # if sum(next_hand) <= 0.1:
                # self.next_hand = pick_weighted(uniform_vec(3))[0]
            # else:
                # normalize(next_hand)
                # self.next_hand = pick_weighted(next_hand)[0]
    
    class HistoryMatch(object):
        def __init__(self, order, *hands):
            self.hands = hands
            self.default_hands = hands[0]
            self.order = order
            self.counts = collections.defaultdict(lambda:None)
        
        def update(self):
            hands_len = len(op_hands)
            for order in xrange(min(self.order, hands_len - 1)):
                index = ()
                for hs in self.hands:
                    index += tuple(hs[-order-2:-1])
                self.counts[index] = (hands_len - 1)
            self.matched_index = None
            for order in xrange(min(self.order, hands_len) - 1, -1, -1):
                index = ()
                for hs in self.hands:
                    index += tuple(hs[-order-1:])
                found = self.counts[index]
                if found is not None:
                    self.matched_index = found
                    break
    
    class HistoryMatchCorrectorBot(object):
        def __init__(self, history_matcher, bot):
            self.history_matcher = history_matcher
            self.bot = bot
            adjustments.append(TIE)
            self.next_hand = bot.next_hand
        
        def update(self):
            matched_index = self.history_matcher.matched_index
            if matched_index is not None:
                nextp = self.history_matcher.default_hands[matched_index]
                old_adjustment = adjustments[matched_index]
                offset = addh[to_win[nextp]][old_adjustment]
            else:
                offset = TIE
            
            self.next_hand = addh[offset][self.bot.next_hand]
            adjustments.append(offset)
    
    class ConstantBot(object):
        def __init__(self, initial_hand):
            self.next_hand = initial_hand
        
        def update(self):
            pass
        
    
    class LastBot(object):
        def __init__(self, initial_hand, ref_hands, diff):
            self.next_hand = initial_hand
            self.ref_hands = ref_hands
            self.diff = diff
        
        def update(self):
            self.next_hand = addh[self.diff][self.ref_hands[-1]]
    
    op_hands = []
    my_hands = []
    payoffs = []
    adjustments = []
    
    
    payoff_counts = HistoryMatch(7, payoffs, adjustments)
    
    initial_hand = random.choice(RPS)
    # constant_bot = ConstantBot(initial_hand)
    # constant_bot = LastBot(initial_hand, my_hands, TIE)
    constant_bot = LastBot(initial_hand, op_hands, WIN)
    
    corrector_bot = HistoryMatchCorrectorBot(payoff_counts, constant_bot)
    
    output = to_str[initial_hand]
    
# --------------------- turn -----------------------------
else:
    my_hands.append(to_num[output])
    op_hands.append(to_num[input])
    payoffs.append(subh[my_hands[-1]][op_hands[-1]])
    hands_played = len(op_hands)
    
    payoff_counts.update()
    constant_bot.update()
    corrector_bot.update()
    
    # if hands_played < 10:
        # print payoffs
        # print corrector_bot.adjustments
    
    # output = to_str[corrector_bot.next_hand]
    output = to_str[corrector_bot.next_hand]