import random

class Markov(object):
  MAX_SUBMOVE = 10
  BEATS = {
      'R': 'P',
      'P': 'S',
      'S': 'R'
      }

  def __init__(self):
    self.moves = []
    self.reset()

  def incrememnt_next_move(self, preceding_moves, move):
    if not preceding_moves in self.next_moves:
      self.next_moves[preceding_moves] = []
    self.next_moves[preceding_moves].append(move)

  def add_moves(self, moves):
    move = moves[-1]
    preceding_moves = tuple(moves[:-1])

    self.incrememnt_next_move(preceding_moves, move)

  def add_move(self, move):
    self.moves.append(move)

    for n in range(self.MAX_SUBMOVE):
      if len(self.moves) > n:
        self.add_moves(self.moves[-(n+2):])

  def reset(self):
    self.next_moves = {}

  def choice(self):
    candiate_moves = ['R', 'P', 'S']

    for n in range(self.MAX_SUBMOVE):
      preceding_moves = tuple(self.moves[-(n+2):])

      if preceding_moves in self.next_moves:
        candiate_moves += self.next_moves[preceding_moves]

    return self.BEATS[random.choice(candiate_moves)]

if input == '':
  markov = Markov()
else:
  markov.add_move(input)

output = markov.choice()