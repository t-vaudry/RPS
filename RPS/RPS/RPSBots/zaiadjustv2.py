# use history matching as the underlying bot to correct upon

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
    
    class HistoryMatchBot(object):
        def __init__(self, initial_hand, history_matcher):
            self.history_matcher = history_matcher
            self.next_hand = initial_hand
        
        def update(self):
            matched_index = self.history_matcher.matched_index
            if matched_index is not None:
                self.next_hand = beats[self.history_matcher.default_hands[matched_index]]
    
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
    
    op_hist = HistoryMatch(7, op_hands, my_hands)
    payoff_counts = HistoryMatch(7, payoffs, adjustments)
    
    initial_hand = random.choice(RPS)
    # constant_bot = ConstantBot(initial_hand)
    # constant_bot = LastBot(initial_hand, my_hands, TIE)
    # constant_bot = LastBot(initial_hand, op_hands, WIN)
    constant_bot = HistoryMatchBot(initial_hand, op_hist)
    
    corrector_bot = HistoryMatchCorrectorBot(payoff_counts, constant_bot)
    
    output = to_str[initial_hand]
    
# --------------------- turn -----------------------------
else:
    my_hands.append(to_num[output])
    op_hands.append(to_num[input])
    payoffs.append(subh[my_hands[-1]][op_hands[-1]])
    hands_played = len(op_hands)
    
    payoff_counts.update()
    op_hist.update()
    constant_bot.update()
    corrector_bot.update()
    
    output = to_str[corrector_bot.next_hand]