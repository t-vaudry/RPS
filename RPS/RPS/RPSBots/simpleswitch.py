# simple, well documented bot
import random

if input == "":
  opp_hist = [] # A list of all played moves by the opponent. 
  
  # score helps to determine the outcome of a round
  score = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1,}
  
  # counter is used to determine a hand, which wins to a given one
  counter = {'P': 'S', 'S': 'R', 'R': 'P'}

  # no information available yet, make a random move 
  output = random.choice(['R', 'P', 'S'])

  # The bot uses three strategies: counter the opponents last moves
  # play a counter to the counter of the bots last move and
  # choose a random move from the opponent and play a counter to it.
 
  # candidates holds the candidate moves of each strategy.
  candidates = [output] *3
  
  # performance holds the info how well the strategy has performed.
  # Once a strategy fails to predict a winning move its performance
  # is set to 0
  performance = [0] * 3

else:
  # Add the opponent move to the list
  opp_hist.append(input)

  # calculate the performance for the last round for each strategy
  for i, c in enumerate(candidates):
    s = score[c+input]
    if s == 1:  # The strategy would have won -> increase performance
      performance[i] += 1
    elif s == -1: # The strategy would have lost -> set its performance to 0 so we won't use it.
      performance[i] = 0

  # now find the best performed strategy and save it to index
  m = max(performance)
  index = performance.index(m)

  # Now we have to set the candidates for each strategy
  
  # Strategy 1:
  # Select a random move from the opponent and counter it.
  # A very simple but effective strategy
  candidates[0] = counter[random.choice(opp_hist)]

  # Strategy 2:
  # counter the opponents last move
  candidates[1] = counter[input]
 
  # Strategy 3:
  # counter to the counter of the bots own last move.
  # This strategy is indented to work against bots which use strategy2
  candidates[2] = counter[counter[output]]

  # Last but not least: set the output with the best strategy
  output = candidates[index]