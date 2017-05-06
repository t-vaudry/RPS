import random
import math
import operator

if input == "":
  hist = []
  moves = ['R', 'P', 'S', 'R', 'P', 'S']
  encode = {'RR': '1', 'PP': '1', 'SS': '1', 'RS': '0', 'SP': '0', 'PR': '0', 'SR': '2', 'PS': '2', 'RP': '2'}
  mylast = None
  output = random.choice(["R", "P", "S"])

elif mylast is None:
  mylast = output
  output = random.choice(["R", "P", "S"])

else:
  hist.append(encode[mylast + input])
  samplesize = int(math.floor(math.sqrt(len(hist))))
  sample = random.sample(hist, samplesize)

  shift = int(max([(e, sample.count(e)) for e in ['0', '1', '2']], key=operator.itemgetter(1))[0])

  toplay = moves[moves.index(mylast) + shift]
  mylast = output
  output = toplay