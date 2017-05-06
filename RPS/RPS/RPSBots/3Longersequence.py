import random
from collections import defaultdict

MAX_LENGTH = 30
MIN_LENGTH = 4
RPS = "RPS"

def InputToInt(x):
  if x == "R":
    return 0
  elif x == "P":
    return 1
  elif x == "S":
    return 2

if input == "": # initialize variables for the first round
  o_history = ""
  o_moves = defaultdict(lambda: [0, 0, 0])
else:
  for i in range(MIN_LENGTH, min(len(o_history) + 1, MAX_LENGTH)):
    s = o_history[-i:]
    o_moves[s][InputToInt(input)] += 1

  o_history += input

best_confidence = 0
best_result = random.choice(RPS)
for i in range(MIN_LENGTH, min(len(o_history) + 1, MAX_LENGTH)):
  s = o_history[-i:]
  if s in o_moves:
    h = o_moves[s]
    order = range(3)
    random.shuffle(order)
    for c in order:
      remaining = [h[x] for x in range(3) if x != c]
      assert len(remaining) == 2
      min_difference = min([h[c] - remaining[x] for x in range(2)])
      if min_difference < 0:
        continue
      ratio = 1.0 * h[c] / (h[0] + h[1] + h[2])
      confidence = ratio * i * i * 4
      if confidence > best_confidence:
        best_confidence = confidence
        best_result = RPS[(c + 1) % 3]

output = best_result