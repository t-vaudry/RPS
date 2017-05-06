import random

def selectBest(s):
  return random.choice([i for i in range(len(s)) if max(s) == s[i]])
  
def selectBestDict(s):
  return random.choice([i for i in s.keys() if max(s.values()) == s[i]])

if not input:
  debug = 0
  
  USE_RANDOM = 1
  USE_HENNY = 1
  USE_MARKOW = 1
  
  LAST_ROUND = 1000
  ROUND = 1
  
  
  history = []
  moves = ["R","P","S"]
  beatedBy = {"R":"P", "P":"S", "S":"R"}
  result = {"R":{"R":0, "P":-1, "S":1}, "P":{"R":1, "P":0, "S":-1}, "S":{"R":-1, "P":1, "S":0}}
  
  M = 0
  
  if USE_RANDOM == 1:
    M += 1
  
  if USE_HENNY == 1:
    M += 6
    
  if USE_MARKOW == 1:
    markov_orders = [0,3,6]
    historyCount = {}
    M += 6 * len(markov_orders)
    
    
  weight = [1] * M
  decay = [0.85] * M
  
  score = [0] * M
  selected = [0] * M
  move = [random.choice(moves) for i in range(M)]
else:
  ROUND += 1
  history += [(last,input)]
  score = [ decay[i] * score[i] + weight[i] * result[move[i]][input] for i in range(M)]
  
  index = 0
  # random optimal
  if USE_RANDOM == 1:
    move[index] = random.choice(moves)
    # adjust random optimal score to zero
    score[index] = 0
    index += 1
  
  first_meta_index = index
  
  if USE_HENNY == 1:
    # henny with meta strategies
    k = random.choice(range(len(history)))
    move[index]   = history[k][0]
    move[index+3] = history[k][1]
    index += 6
    
  if USE_MARKOW == 1:
    # markow with meta strategies
    for m in markov_orders:
      if len(history) > m:
        key = tuple(history[-m-1:-1])
        if not (key in historyCount):
          historyCount[key] = [{"R":0,"P":0,"S":0},{"R":0,"P":0,"S":0}]
        historyCount[key][0][history[-1][0]] += 1
        historyCount[key][1][history[-1][1]] += 1
        
    for m in markov_orders:
      if len(history) >= m:
        key = tuple(history[-m:])
        if key in historyCount:
          move[index]   = selectBestDict(historyCount[key][0])
          move[index+3] = selectBestDict(historyCount[key][1])
        else:
          move[index]   = random.choice(moves)
          move[index+3] = random.choice(moves)
      else:
        move[index]   = random.choice(moves)
        move[index+3] = random.choice(moves)
      index += 6
    
  # set other meta strategies
  for i in range(first_meta_index, M, 3):
    move[i+1] = beatedBy[move[i]]
    move[i+2] = beatedBy[move[i+1]]
  
best = selectBest(score)
selected[best] += 1
output = move[best]
last = output

if debug == 1:
  if ROUND == LAST_ROUND:
    print "score =", score
    print "selected =", selected