# rewrite with less functions and more dictionaries which are faster
# trying out a slightly different mixing which uses a different scoring
# also allow strategies to return None to indicate no prediction
# also changed a strategy's behaviour to allow multiple users

# --------------------- initialization -----------------------------
if not input:
   import random, math
   import collections, itertools, operator, functools

   ROUNDS = 1000
   R, P, S = 0, 1, -1
   RPS = [R, P, S]
   TIE, WIN, LOSE = 0, 1, -1
   OUTCOMES = [TIE, WIN, LOSE]
   
   to_num = {'R':R, 'P':P, 'S':S}
   to_str = ['R', 'P', 'S']
   
   play = [[TIE, LOSE, WIN], [WIN, TIE, LOSE], [LOSE, WIN, TIE]]
   unplay = [[R, P, S], [P, S, R], [S, R, P]]
   ties = unplay[TIE]
   beats = unplay[WIN]
   loses = unplay[LOSE]

   def normalize(pvec):
      total = sum(pvec)
      for i in xrange(len(pvec)):
         pvec[i] /= total
   
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
         self.next_hands = [uniform_pvec(3) for n in xrange(self.bot_num)]
         self.scores = [None] * self.bot_num
         self.next_hand = None
      
      def update(self):
         # update scores
         op_last_hand = op_hands[-1]
         for i in xrange(self.bot_num):
            last_hand = self.next_hands[i]
            if last_hand is None:
               continue
            outcome = [last_hand[ties[op_last_hand]], last_hand[beats[op_last_hand]], last_hand[loses[op_last_hand]]]
            if outcome[LOSE] > outcome[WIN] and self.dropswitch:
               self.scores[i] = None
            else:
               curr_score = self.scores[i]
               if curr_score is None:
                  self.scores[i] = outcome
               else:
                  new_weight = 1.0 - self.decay
                  for s in OUTCOMES:
                     curr_score[s] = curr_score[s] * self.decay + outcome[s] * new_weight
        
         # compute next hand
         next_hand = [0.0] * 3
         for i in xrange(self.bot_num):
            bot_next_hand = self.bots[i].next_hand
            self.next_hands[i] = bot_next_hand
            if bot_next_hand is None:
               continue
            curr_score = self.scores[i]
            pscore = curr_score[WIN]
            for h in RPS:
               next_hand[h] += bot_next_hand[h] * pscore
            pscore = curr_score[TIE]
            for h in RPS:
               next_hand[h] += bot_next_hand[loses[h]] * pscore
            pscore = curr_score[LOSE]
            for h in RPS:
               next_hand[h] += bot_next_hand[beats[h]] * pscore
         if sum(next_hand) == 0.0:
            self.next_hand = uniform_pvec(3)
         else:
            normalize(next_hand)
            self.next_hand = next_hand
   
   class LastOpBot(object):
      def __init__(self, d):
         self.d = d
      
      def update(self):
         hand_weights = [0.0] * 3
         hand_weights[unplay[self.d][op_hands[-1]]] = 1.0
         self.next_hand = hand_weights
   
   # just plays against the op's last move
   class LastMyBot(object):
      def __init__(self, d):
         self.d = d
      
      def update(self):
         hand_weights = [0.0] * 3
         hand_weights[unplay[self.d][my_hands[-1]]] = 1.0
         self.next_hand = hand_weights
   
   class RandomBot(object):
      def update(self):
         self.next_hand = [1.0/3.0] * 3
   
   op_last_bot = [LastOpBot(TIE), LastOpBot(WIN), LastOpBot(LOSE)]
   my_last_bot = [LastMyBot(TIE), LastMyBot(WIN), LastMyBot(LOSE)]
   mixer_op_last = Mixer(0.6, False, *op_last_bot)
   mixer_my_last = Mixer(0.7, False, *my_last_bot)
   
   # mixer = Mixer(0.8, False, my_last_bot_fast, my_last_bot, op_last_bot, RandomBot())
   mixer = Mixer(0.6, False, mixer_op_last, mixer_my_last)
   # mixer = mixer_op_last
   
   my_hands = []
   op_hands = []
   
   next_hand = random.choice(RPS)
   output = to_str[next_hand]
   my_hands.append(next_hand)
   
# --------------------- turn -----------------------------
else:
   op_hands.append(to_num[input])
   
   hands_played = len(my_hands)
   
   for bot in op_last_bot:
      bot.update()
   mixer_op_last.update()
   
   for bot in my_last_bot:
      bot.update()
   mixer_my_last.update()
   
   mixer.update()
   
   next_hand_weights = mixer.next_hand
   if sum(next_hand_weights) <= 0:
      next_hand = random_hand()
   else:
      next_hand = pick_weighted(next_hand_weights)[0]
   output = to_str[next_hand]
   my_hands.append(next_hand)
   
   # if hands_played < 10:
      # print(mixer.scores)
      # print(next_hand_weights)
      # print(next_hand)