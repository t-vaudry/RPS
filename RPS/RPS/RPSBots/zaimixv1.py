# mixes 3 main strategies, constant, beat last, history highest order match
# and the 6 variations of using each strategy (except for constant, which only has 3)

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
    
    def empty_vec(n):
        return [0.0] * n

    def uniform_vec(n):
        return [1.0 / n] * n
    
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
            self.prediction = None
            for order in xrange(min(self.order, hands_len)-1, -1, -1):
                index = tuple(self.all[-order-1:])
                past = self.counts[index]
                if past:
                    self.prediction = self.decode3(past[-1])
                    break
        
        def decode3(self, code):
            hands = []
            for i in xrange(self.handss_num):
                hands.append(code % 3)
                code /= 3
            return hands
    
    # mixes multiple strategies
    class Mixer(object):
        def __init__(self, op_moves, decay, dropswitch, *bots):
            self.op_moves = op_moves
            self.bots = bots
            self.bot_num = len(self.bots)
            self.decay = decay
            self.dropswitch = dropswitch
            self.next_hands = [None] * self.bot_num
            self.scores = [None] * self.bot_num
            self.next_hand = bots[0].next_hand
      
        def update(self):
            # update scores
            op_last_hand = self.op_moves[-1]
            for i in xrange(self.bot_num):
                last_hand = self.next_hands[i]
                if last_hand is None:
                    continue
                score = scorep[subh[last_hand][op_last_hand]]
                if score < 0 and self.dropswitch:
                    self.scores[i] = None
                else:
                    if self.scores[i] is None:
                        self.scores[i] = score * (1 - self.decay)
                    else:
                        self.scores[i] *= self.decay
                        self.scores[i] += score
         
            # compute next hand
            next_hand = empty_vec(3)
            for i in xrange(self.bot_num):
                bot_next_hand = self.bots[i].next_hand
                self.next_hands[i] = bot_next_hand
                if bot_next_hand is None:
                    continue
                curr_score = self.scores[i]
                if curr_score is None or curr_score < 0:
                    continue
                next_hand[bot_next_hand] += curr_score
            if sum(next_hand) <= 0.1:
                self.next_hand = pick_weighted(uniform_vec(3))[0]
            else:
                normalize(next_hand)
                self.next_hand = pick_weighted(next_hand)[0]
    
    class HistoryBot(object):
        def __init__(self, handix, history):
            self.handix = handix
            self.history = history
        
        def update(self):
            if self.history.prediction is None:
                self.next_hand = None
            else:
                self.next_hand = self.history.prediction[self.handix]
    
    class ConstantBot(object):
        def __init__(self, op_moves, my_moves):
            self.next_hand = my_moves[-1]
        
        def update(self):
            pass
    
    class BeatLastBot(object):
        def __init__(self, op_moves, my_moves):
            self.op_moves = op_moves
        
        def update(self):
            self.next_hand = self.op_moves[-1]
    
    class OffsetBot(object):
        def __init__(self, bot, offset):
            self.bot = bot
            self.offset = offset
        
        def update(self):
            if self.bot.next_hand is None:
                self.next_hand = None
            else:
                self.next_hand = addh[self.offset][self.bot.next_hand]
    
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
        constantbot = ConstantBot(op_hands, my_hands)
        constantbotW = OffsetBot(constantbot, W)
        constantbotL = OffsetBot(constantbot, L)
        
        beatlastbot = BeatLastBot(op_hands, my_hands)
        beatlastbotW = OffsetBot(beatlastbot, W)
        beatlastbotL = OffsetBot(beatlastbot, L)
        
        beatlastbot2 = BeatLastBot(my_hands, op_hands)
        beatlastbot2W = OffsetBot(beatlastbot2, W)
        beatlastbot2L = OffsetBot(beatlastbot2, L)
        
        history = History(7, op_hands, my_hands)
        
        histbot = HistoryBot(0, history)
        histbotW = OffsetBot(histbot, W)
        histbotL = OffsetBot(histbot, L)
        
        histbot2 = HistoryBot(1, history)
        histbot2W = OffsetBot(histbot, W)
        histbot2L = OffsetBot(histbot, L)
        
        mixer = Mixer(op_hands, 0.95, False,
            constantbot, constantbotW, constantbotL,
            beatlastbot, beatlastbotW, beatlastbotL,
            beatlastbot2, beatlastbot2W, beatlastbot2L,
            histbot, histbotW, histbotL,
            histbot2, histbot2W, histbot2L)
    
    constantbot.update()
    constantbotW.update()
    constantbotL.update()
    
    beatlastbot.update()
    beatlastbotW.update()
    beatlastbotL.update()
    
    beatlastbot2.update()
    beatlastbot2W.update()
    beatlastbot2L.update()
    
    history.update()
    
    histbot.update()
    histbotW.update()
    histbotL.update()
    
    histbot2.update()
    histbot2W.update()
    histbot2L.update()
    
    mixer.update()
    
    output = convert[mixer.next_hand]