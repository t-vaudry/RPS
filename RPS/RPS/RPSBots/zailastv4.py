# like zai_last series but looks at my hands and op hands
# added drop switching as an option to the mixer
# mixes 3 strategies now

# --------------------- initialization -----------------------------
if not input:
   import random
   import math
   import itertools, operator, functools
   
   # constants
   ROUNDS = 1000
   R, P, S = 0, 1, 2
   RPS_NUM = (R, P, S)
   RPS_STR = 'RPS'
   WIN, TIE, LOSE = 1, 0, -1
   
   def to_num(h):
      return RPS_STR.index(h)

   def to_str(i):
      return RPS_STR[i]
   
   def random_hand():
      return random.choice(RPS_NUM)
   
   def play(h1, h2):
      return (h1 - h2 + 4) % 3 - 1

   def diff(h1, h2):
      return (h1 - h2 + 3) % 3

   def undiff(h, d):
      return (h + d + 3) % 3

   def beats(h):
      return undiff(h, WIN)

   def loses(h):
      return undiff(h, LOSE)

   def ties(h):
      return undiff(h, TIE)
   
   def normalize(lst):
      total = float(sum(lst))
      if total <= 0.0:
         total = 1.0
      return [x / total for x in lst]
   
   def pick_random(lst):
      i = random.randint(0, len(lst) - 1)
      return (i, lst[i])

   def my_max(val1, val2):
      return val1 if val1[1] > val2[1] else val2

   def pick_max(lst):
      return reduce(my_max, enumerate(lst))

   def pick_weighted(lst, sumlst=None):
      r = random.uniform(0.0, sumlst or sum(lst))
      acc = 0.0
      for i, w in enumerate(lst):
         acc += w
         if r <= acc:
            return (i, w)
   
   # sliding window counter of a sequence of 0,1,2s
   # class Counter3(object):
      # def __init__(self, seq, period):
         # self.seq = seq
         # self.period = period
         # self.width = 0
         # self.counts = [0] * 3
      # def update(self):
         # self.counts[self.seq[-1]] += 1
         # self.width += 1
         # if self.width > self.period:
            # self.counts[self.seq[-self.period]] -= 1
      # def ratios(self):
         # return tuple(c / float(self.width) for c in self.counts)
   
   # mixes multiple strategies
   class Mixer(object):
      def __init__(self, decay, dropswitch, *bots):
         self.bots = bots
         self.bot_num = len(self.bots)
         self.decay = decay
         self.dropswitch=dropswitch
         self.next_hands = [[0.0] * 3 for n in xrange(self.bot_num)]
         self.scores = [0.0] * self.bot_num
      
      def _update_scores(self):
         op_last_hand = op_hands[-1]
         for i in xrange(self.bot_num):
            last_score = 0.0
            for h in RPS_NUM:
               last_score += self.next_hands[i][h] * play(h, op_last_hand)
            if last_score < 0.0 and self.dropswitch:
               self.scores[i] = 0.0
            else:
               self.scores[i] *= self.decay
               self.scores[i] += last_score
      
      def next_hand(self):
         self._update_scores()
         
         next_hand = [0.0] * 3
         for i in xrange(self.bot_num):
            bot_next_hand = self.bots[i].next_hand()
            self.next_hands[i] = bot_next_hand
            if self.scores[i] < 0.0:
               # if this bot has a negative score, then play against it
               m = WIN
            else:
               m = TIE
            for h in RPS_NUM:
               next_hand[h] += bot_next_hand[undiff(h, m)] * abs(self.scores[i])
         return normalize(next_hand)
   
   class LastOpBot(object):
      def __init__(self, d):
         self.d = d
      
      def next_hand(self):
         hand_weights = [0.0] * 3
         hand_weights[undiff(op_hands[-1], self.d)] = 1.0
         return hand_weights
   
   # just plays against the op's last move
   class LastMyBot(object):
      def __init__(self, d):
         self.d = d
      
      def next_hand(self):
         hand_weights = [0.0] * 3
         hand_weights[undiff(my_hands[-1], self.d)] = 1.0
         return hand_weights
   
   class RandomBot(object):
      def next_hand(self):
         return [1.0/3.0] * 3
   
   my_last_bot_fast = Mixer(0.96, True, LastMyBot(WIN), LastMyBot(TIE), LastMyBot(LOSE))
   my_last_bot = Mixer(0.6, False, LastMyBot(WIN), LastMyBot(TIE), LastMyBot(LOSE))
   # mixer_op_last = Mixer(0.96, True, LastOpBot(WIN), LastOpBot(TIE), LastOpBot(LOSE))
   op_last_bot = Mixer(0.8, False, LastOpBot(WIN), LastOpBot(TIE), LastOpBot(LOSE))
   
   mixer = Mixer(0.8, False, my_last_bot_fast, my_last_bot, op_last_bot, RandomBot())
   # mixer.scores[0] = 1
   # mixer = mixer_my_last
   
   my_hands = []
   op_hands = []
   
   next_hand = random_hand()
   output = to_str(random_hand())
   my_hands.append(next_hand)
   
# --------------------- turn -----------------------------
else:
   op_hands.append(to_num(input))
   
   hands_played = len(my_hands)
   
   next_hand_weights = mixer.next_hand()
   if sum(next_hand_weights) <= 0:
      next_hand = random_hand()
   else:
      next_hand = pick_weighted(next_hand_weights)[0]
   output = to_str(next_hand)
   my_hands.append(next_hand)
   
   # if hands_played < 10:
      # print(mixer.scores)
      # print(next_hand_weights)
      # print(next_hand)