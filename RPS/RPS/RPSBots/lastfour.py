from collections import deque
import operator
import random

class LastFour:
    name = "LastFour"
    def reset(self):
        self.mydeque = deque()
        self.oppdeque = deque()
        self.played_dict = {}

    def get_key(self, size=4):
        key = (tuple(list(self.mydeque)[-size:]),  tuple(list(self.oppdeque)[-size:]))
        return key

    def get_move(self):
        if len(self.mydeque) < 4:
            return random.choice(["R", "P", "S"])
        for keysize in range(4, 0, -1):
            key = self.get_key(size=keysize)
            played = self.played_dict.get(key, None)
            if played:
                idx, _ = max(enumerate(played), key=operator.itemgetter(1)) 
                expected = self.hand_by_index(idx)
                return self.anti_expected(expected) 
        return random.choice(["R", "P", "S"])

    def anti_expected(self, expected):
        """Returns a winning move against the expected one"""
        return {None: 'P', 'R': 'P', 'P': 'S', 'S':'R'}[expected]

    def index(self, hand):
        return ['R', 'P', 'S'].index(hand)

    def hand_by_index(self, index):
        return ['R', 'P', 'S'][index]

    def inform_played(self, opp, my):
        if len(self.mydeque) == 4:
            for keysize in range(4, 0, -1):
                played = self.played_dict.get(self.get_key(size=keysize), [0,0,0,0])
                played[self.index(opp)] += 1
                self.played_dict[self.get_key(size=keysize)] = played

        self.mydeque.append(my)
        self.oppdeque.append(opp)

        if len(self.mydeque) > 4:
            self.mydeque.popleft()

        if len(self.oppdeque) > 4:
            self.oppdeque.popleft()

if input == '':
    bot = LastFour()
    bot.reset()
else:
    try:
        out = output
        if not out in ["R", "P", "S"]:
            raise
        bot.inform_played(input, out)
    except:
        pass

output = bot.get_move()