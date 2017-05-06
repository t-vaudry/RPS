import random

class Markov(object):
  MAX_SUBMOVE = 10
  BEATS = {
      'R': 'P',
      'P': 'S',
      'S': 'R'
      }

  def __init__(self):
    self.e_moves = []
    self.s_moves = []
    self.next_moves = {}

  def incrememnt_next_move(self, preceding_moves, move):
    if not preceding_moves in self.next_moves:
      self.next_moves[preceding_moves] = []
    self.next_moves[preceding_moves].append(move)

  def add_moves(self, moves, move):
    preceding_moves = tuple(moves[:-1])

    self.incrememnt_next_move(preceding_moves, move)

  def learn(self):
    for n in range(self.MAX_SUBMOVE):
      if len(self.e_moves) > n:
        preceding_moves = (tuple(self.e_moves[-(n+2):-1]), tuple(self.s_moves[-(n+2):]))
        move = self.e_moves[-1]
        self.add_moves(preceding_moves, move)

  def choice(self):
    candiate_moves = ['R', 'P', 'S']

    for n in range(self.MAX_SUBMOVE):
      if len(self.e_moves) > n:
        preceding_moves = (tuple(self.e_moves[-(n+2):]), tuple(self.s_moves[-(n+2):]))
        move = self.e_moves[-1]

        if preceding_moves in self.next_moves:
          candiate_moves += self.next_moves[preceding_moves]

    return self.BEATS[random.choice(candiate_moves)]


output = random.choice('R')

if input == '':
  markov = Markov()
else:
  output = markov.choice()

markov.e_moves.append(input)
markov.s_moves.append(output)
markov.learn()