# added differentiating between a WIN,TIE,LOSE of the last hand

# --------------------- initialization -----------------------------
if not input:
   import random, math
   import collections, itertools, operator

   ROUNDS = 1000
   MODULUS = 3
   R, P, S = 0, 1, -1
   RPS = [R, P, S]
   TIE, WIN, LOSE = R, P, S
   PAYOFFS = [TIE, WIN, LOSE]
   to_num = {'R':R, 'P':P, 'S':S}
   to_str = ['R', 'P', 'S']
   subh = [[TIE, LOSE, WIN], [WIN, TIE, LOSE], [LOSE, WIN, TIE]]
   addh = [[R, P, S], [P, S, R], [S, R, P]]
   ties = addh[TIE]
   beats = addh[WIN]
   loses = addh[LOSE]
   
   def predictability(pvec):
      value = 0.0
      last_ix = len(pvec) - 1
      for i in xrange(last_ix):
         for j in xrange(last_ix, i, -1):
            value += abs(pvec[i] - pvec[j])
      return value
   
   def normalize(pvec):
      total = sum(pvec)
      for i in xrange(len(pvec)):
         pvec[i] /= total
   
   def empty_pvec(n):
      return [0.0] * n
   
   def uniform_pvec(n):
      return [1.0 / n] * n

   def pick_weighted(pvec):
      u = random.random()
      acc = 0.0
      for i, p in enumerate(pvec):
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
                  new_weight = 1.0 - self.decay
                  for s in PAYOFFS:
                     curr_score[s] = curr_score[s] * self.decay + payoff[s] * new_weight
         
         # compute next hand
         next_hand = empty_pvec(MODULUS)
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
            # if hands_played > 100 and hands_played < 105:
               # print(i, curr_score)
               # print(i, bot_next_hand)
            for s in PAYOFFS:
               pscore = curr_score[s] * nonrandomness
               offset = addh[LOSE][s]
               for h in RPS:
                  next_hand[h] += bot_next_hand[addh[offset][h]] * pscore
         if sum(next_hand) <= 0.1:
            self.next_hand = uniform_pvec(MODULUS)
         else:
            normalize(next_hand)
            self.next_hand = next_hand
   
   class LastHandBot(object):
      def __init__(self, hand_history, payoff_history, diffs):
         self.hand_history = hand_history
         self.payoff_history = payoff_history
         self.diffs = diffs
      
      def update(self):
         next_hand_pvec = empty_pvec(MODULUS)
         next_hand_pvec[addh[self.diffs[self.payoff_history[-1]]][self.hand_history[-1]]] = 1.0
         self.next_hand = next_hand_pvec
   
   # history tracking
   my_hands = []
   op_hands = []
   my_diffs = []
   op_diffs = []
   payoffs = []
   
   last_bots = [LastHandBot(my_hands, payoffs, [0,0,0]),
                LastHandBot(my_hands, payoffs, [0,0,1]),
                LastHandBot(my_hands, payoffs, [0,0,-1]),
                LastHandBot(my_hands, payoffs, [0,1,0]),
                LastHandBot(my_hands, payoffs, [0,-1,0]),
                LastHandBot(my_hands, payoffs, [1,0,0]),
                LastHandBot(my_hands, payoffs, [-1,0,0]),
                LastHandBot(my_hands, payoffs, [0,1,-1]),
                LastHandBot(my_hands, payoffs, [0,-1,1])]
   
   mixer_slow = Mixer(0.95, False, *last_bots)
   mixer_fast = Mixer(0.6, False, *last_bots)
   
   mixer = Mixer(0.6, False, mixer_fast, mixer_slow)
   
   next_hand = random.choice(RPS)
   output = to_str[next_hand]
   my_hands.append(next_hand)
   
# --------------------- turn -----------------------------
else:
   op_hands.append(to_num[input])
   payoffs.append(subh[my_hands[-1]][op_hands[-1]])
   my_diffs.append(my_hands[-1] if len(my_hands) == 1 else subh[my_hands[-1]][my_hands[-2]])
   op_diffs.append(op_hands[-1] if len(op_hands) == 1 else subh[op_hands[-1]][op_hands[-2]])
   
   hands_played = len(my_hands)
   
   for b in last_bots:
      b.update()
   
   mixer_slow.update()
   mixer_fast.update()
   
   # if hands_played % 98 == 0:
      # print(op_hands[-1], payoffs[-1])
      # print(op_hands[-1])
      # print(op_history.matches)
      # print(op_history.info_counts)
   
   mixer.update()
   # if hands_played > 100 and hands_played < 105:
      # print(mixer.next_hand)
      # print(op_hands[-1])
   next_hand = pick_weighted(mixer.next_hand)[0]
   output = to_str[next_hand]
   my_hands.append(next_hand)
   
   # if hands_played < 10:
      # print(mixer.scores)
      # print(next_hand_weights)
      # print(next_hand)