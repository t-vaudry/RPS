# bot built through a genetic algorithm
# generation 1320 track 2
# only slightly worse than random, through the power of science!
import random

if input == "":
    class GenBot:
        def __init__(self, code=None):
            self.code = code

            self.idx = 0
            self.stack = []
            self.last_input = ""

        def failure(self, msg):
            # nowhere to send msg...so just keep retrying!
            self.reset_stack()

        def reset_stack(self):
            self.idx = 0
            self.stack = []

        def push_stack(self, idx):
            self.stack.append(idx)

        def pop_stack(self):
            if self.stack:
                return self.stack.pop()
            else:
                return 0

        def goto(self, idx, comeback=False):
            if comeback:
                newidx = self.idx+1
                if newidx > len(self.code)-1:
                    newidx = 0
                self.push_stack(newidx)

            self.idx = idx

        def new_game(self):
            self.idx = 0
            self.reset_stack()

        def get_move(self, input):
            self.last_input = input

            done = False
            result = ""
            noresults = 0
            while not done:
                if self.idx >= len(self.code):
                    self.idx = self.pop_stack()
                    if self.idx >= len(self.code):
                        self.failure("Busted index")
                        continue

                move = self.code[self.idx][0]
                extra = self.code[self.idx][1]

                if move in "RPS":
                    result = move
                elif move in "GH":
                    # goto here (and come back if H)
                    comeback = False
                    if move == "H":
                        comeback = True
                    self.goto(extra["idx"], comeback=comeback)
                    continue
                elif move == "X":
                    # stop / return
                    self.idx = self.pop_stack()
                    continue
                elif move in "IJ":
                    # if input == extra["move"] then goto (and comeback if J)
                    comeback = False
                    if move == "J":
                        comeback = True
                    if input == extra["move"]:
                        self.goto(extra["idx"], comeback=comeback)
                        continue
                elif move in "YZ":
                    comeback = False
                    if move == "Z":
                        comeback = True
                    # random chance to goto location
                    if random.random() > extra["chance"]:
                        self.goto(extra["idx"], comeback=comeback)

                self.idx += 1

                if result:
                    done = True
                else:
                    noresults += 1
                    if noresults > 100:
                        self.failure("Too many loops")
            return result

    code = [['G', {'idx': 2}], ('X', {}), ('G', {'idx': 10}), ['P', {}], ('P', {}), ('P', {}), ('X', {}), ('X', {}), ('J', {'move': 'S', 'idx': 1}), ('S', {}), ['Y', {'chance': 0.64402128133388381, 'idx': 8}], ('Y', {'chance': 0.43930114281376154, 'idx': 4}), ('R', {})]
    bot = GenBot(code)
output = bot.get_move(input)