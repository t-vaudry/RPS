# Copyright Josh Souza 2015
# Devlopment@pureinsomnia.com
# Wow, this is a stupid attempt number two based on probabilities, and has lots of crap code
import random
# ORDER HERE MATTERS! going X-1 will be a winning direction
options=["S","P","R"]
def beat(input):
  return options[options.index(input)-1]


def who_won(them,me):
  if them==me:
    return 0
  if beat(them)==me:
    return 1
  return -1

# Main script code starts here

if input == "": # not in options:
  # Game beginning
  input_log = []
  output_log = []
  #choices = {}
  #for o in options:
  #  choices[o]={}
  #  for p in options:
  #    choices[o][p]=0
else:
  input_log.insert(0,input)
  #choices[input_log[0]][output_log[0]] = who_won(input_log[0],output_log[0])



if len(input_log) == 0:
  output = random.choice(options)

else:
  counts = {}
  last_ten = {}
  prob_repeat = {}
  prob_repeat_ten = {}
  games = 0
  last_ten_games = 0
  for c in options:  
    counts[c] = input_log.count(c)
    last_ten[c] = input_log[10:].count(c) # Last ten games ratios
    games = games + counts[c]
    last_ten_games = last_ten_games + last_ten[c]

  final_choices = []
  weights = {"games":{"scope": input_log,"weight":30},
             "last_25_percent":{"scope": input_log[:1+len(input_log)/5],"weight":10},
             #"last_25_percent":{"scope": output_log[-1*len(output_log)/5:],"weight":10},
             "last_10":{"scope": input_log[:10],"weight":10},
             "last_3":{"scope": input_log[:3],"weight":20},
            }
  for weight in weights:
    counts = {}
    games = 0
    for c in options:
      counts[c] = weights[weight]["scope"].count(c)
      games = games + counts[c]
    for c in options:
      prob_repeat[c] = counts[c] / 1.0 / games
      prob_repeat[c] = (1 - prob_repeat[c]) * weights[weight]["weight"]
      for i in range(int(prob_repeat[c])):
        final_choices.append(beat(beat(c)))
  random.shuffle(final_choices)
  # final_choices is what I am betting they will pick
  output=random.choice(final_choices)

  #output = input
output_log.insert(0,output)