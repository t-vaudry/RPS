# tries to find the period in which playing one strategy will lose
# then use that period to keep switching strategies right before losing

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
    
    
    class Bot(object):
        def __init__(self, op_moves, initial_move, bookkeeping):
            self.op_moves = op_moves
            self.next_hand = initial_move
            self.bookkeeping = bookkeeping
            if self.bookkeeping:
                self.my_moves = []
                self.payoffs = []
        
        def update(self):
            # update some stats and bookkeeping
            if self.bookkeeping:
                self.my_moves.append(self.next_hand)
                self.payoffs.append(subh[self.my_moves[-1]][self.op_moves[-1]])
            
    
    class BotWrap(Bot):
        def __init__(self, op_moves, initial_move, bookkeeping, bot, offset):
            super(BotWrap, self).__init__(op_moves, initial_move, bookkeeping)
            self.bot = bot
            self.offset = offset
        
        def addoffset(self, offset):
            self.offset = addh[offset][self.offset]
        
        def update(self):
            super(BotWrap, self).update()
            self.next_hand = addh[self.offset][self.bot.next_hand]
    
    class ConstantBot(Bot):
        def __init__(self, op_moves, initial_move, bookkeeping):
            super(ConstantBot, self).__init__(op_moves, initial_move, bookkeeping)
    
    class LastBot(Bot):
        def __init__(self, op_moves, initial_move, bookkeeping, ref_list, offset):
            super(LastBot, self).__init__(op_moves, initial_move, bookkeeping)
            self.ref_list = ref_list
            self.offset = offset
        
        def update(self):
            super(LastBot, self).update()
            self.next_hand = addh[self.offset][self.ref_list[-1]]
    
    op_hands = []
    my_hands = []
    payoffs = []
    
    initial_hand = random.choice(RPS)
    
    constantbot = ConstantBot(op_hands, initial_hand, False)
    wrappedbot = BotWrap(op_hands, initial_hand, False, constantbot, TIE)
    
    cycle_length = 1000
    cycle_acc = 1
    cycle_lengths = []
    
    output = to_str[constantbot.next_hand]
# --------------------- turn -----------------------------
else:
    my_hands.append(to_num[output])
    op_hands.append(to_num[input])
    payoffs.append(subh[my_hands[-1]][op_hands[-1]])
    hands_played = len(op_hands)
    
    if cycle_acc >= cycle_length:
        wrappedbot.addoffset(LOSE)
    else:
        last_payoff = payoffs[-1]
        if last_payoff == WIN or last_payoff == TIE:
            cycle_acc += 1
        else:
            if cycle_acc == 0:
                wrappedbot.addoffset(TIE)
                cycle_acc = 1
            else:
                wrappedbot.addoffset(LOSE)
                cycle_length = cycle_acc
                cycle_lengths.append(cycle_length)
                cycle_acc = 0
        
    
    constantbot.update()
    wrappedbot.update()
    
    output = to_str[wrappedbot.next_hand]
    
    # if hands_played == 999:
        # print (','.join(map(str,cycle_lengths)))