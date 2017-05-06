# similar to zai_counts_combo series, but uses the new mixing strategy
# may not be as good as zai_counts_combo series

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
   
   # class LastHandBot(object):
      # def __init__(self, hand_history, payoff_history, payoff_filter, diff):
         # self.hand_history = hand_history
         # self.payoff_history = payoff_history
         # self.payoff_filter = payoff_filter
         # self.addoffset = addh[diff]
      
      # def update(self):
         # if self.payoff_history[-1] in self.payoff_filter:
            # next_hand_pvec = empty_pvec(MODULUS)
            # next_hand_pvec[self.addoffset[self.hand_history[-1]]] = 1.0
            # self.next_hand = next_hand_pvec
         # else:
            # self.next_hand = None

   # POWER3 = [MODULUS ** n for n in xrange(10)]
   
   def empty_counts():
      return [empty_pvec(MODULUS) for m in xrange(MODULUS)]
      # return empty_pvec(MODULUS)
   
   def match_weight(hand_num, order):
      return 10 ** (hand_num / 100.0) * 10 ** (order / 7.0)
      # return hand_num * 7
      # return 1.0
   
   class HistoryMatch(object):
      def __init__(self, max_order, matchlist, splitlist, countlist, match_weight):
         self.max_order = max_order
         self.matchlist = matchlist
         self.splitlist = splitlist
         self.countlist = countlist
         self.matches = collections.defaultdict(empty_counts)
         self.match_weight = match_weight
      
      def update(self):
         length = len(self.matchlist)
         # update the payoff counts
         for i in xrange(min(self.max_order + 1, length)):
            update_match = tuple(self.matchlist[-i-1:-1])
            update_weight = self.match_weight(length, i)
            update_split = self.splitlist[-1]
            update_count = self.countlist[-1]
            self.matches[update_match][update_split][update_count] += update_weight
         # set up information to be used in prediction
         info_counts = [empty_counts() for n in xrange(self.max_order+1)]
         for i in xrange(min(self.max_order + 1, length + 1)):
            curr_match = tuple(self.matchlist[-i:] if i != 0 else [])
            curr_counts = self.matches[curr_match]
            for s in RPS:
               for h in RPS:
                  info_counts[i][s][h] += curr_counts[s][h]
         self.info_counts = info_counts
   
   class HistoryMatchBot(object):
      def __init__(self, history_matcher, hands, split):
         self.history_matcher = history_matcher
         self.hands = hands
         self.split = split
      
      def update(self):
         curr_counts = empty_pvec(MODULUS)
         info_counts = self.history_matcher.info_counts
         for i in xrange(self.history_matcher.max_order + 1):
            for h in RPS:
               curr_counts[h] += info_counts[i][self.split][h]
         next_hand_pvec = [curr_counts[subh[h][self.hands[-1]]] for h in RPS]
         if sum(next_hand_pvec) < 0.1:
            next_hand_pvec = None
         else:
            normalize(next_hand_pvec)
         self.next_hand = next_hand_pvec
      
   # history tracking
   my_hands = []
   op_hands = []
   my_diffs = []
   op_diffs = []
   payoffs = []
   
   my_history = HistoryMatch(7, my_diffs, payoffs, my_diffs, match_weight)
   op_history = HistoryMatch(7, op_diffs, payoffs, op_diffs, match_weight)
   # payoff_history = HistoryMatch(7, payoffs, my_diffs, match_weight)
   
   op_history_bot = ([HistoryMatchBot(op_history, op_hands, s) for s in PAYOFFS])
   my_history_bot = ([HistoryMatchBot(my_history, my_hands, s) for s in PAYOFFS])
   
   mixer = Mixer(0.6, False, *(op_history_bot + my_history_bot))
   # mixer = Mixer(0.6, False, *my_history_bot)
   
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
   
   my_history.update()
   op_history.update()
   # payoff_history.update()
   
   for b in op_history_bot:
      b.update()
   for b in my_history_bot:
      b.update()
   # my_history_bot.update()
   
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