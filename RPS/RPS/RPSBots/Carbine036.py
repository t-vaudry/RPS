#Carbine.py, an [hopefully] intelligent RPS prediction AI.
import random

ROCK = "R"
PAPER = "P"
SCISSOR = "S"
MAX_CYCLE = 6
MIN_CYCLE = 3

output = ""

if input == "":
  history = []
  patterns = {}
else:
  history.append(input)


#Build heuristic table
#Dict of pattern {"<pattern>" : {R:#, P:#, S:#}}
for i in range(MIN_CYCLE, MAX_CYCLE):
  if (len(history) <= MIN_CYCLE) or (i >= len(history)):
    continue

  seq = "".join(history[-i:-1])
  weight = patterns.get(seq, {ROCK:0, PAPER:0, SCISSOR:0})
  weight[input] += 1
  patterns[seq] = weight



#Now tally up the weights for R, P, and S based on the updated heuristics
r, p, s = (0, 0, 0)
for i in range(MIN_CYCLE, MAX_CYCLE):
  if (len(history) <= MIN_CYCLE) or (i >= len(history)):
    continue
  seq = "".join(history[-i:-1])
  r += patterns.get(seq, {ROCK:0, PAPER:0, SCISSOR:0})[ROCK] * (MAX_CYCLE - len(seq))
  p += patterns.get(seq, {ROCK:0, PAPER:0, SCISSOR:0})[PAPER] * (MAX_CYCLE - len(seq))
  s += patterns.get(seq, {ROCK:0, PAPER:0, SCISSOR:0})[SCISSOR] * (MAX_CYCLE - len(seq))

if (r > p) and (r > s):
  output = PAPER
elif p > s:
  output = SCISSOR
elif (s != p) and (s != r):
  output = ROCK
else:
  output = random.choice([ROCK, PAPER, SCISSOR])

if output == "":
  output = random.choice([ROCK, PAPER, SCISSOR])