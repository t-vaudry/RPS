import random
import math

def ans(hand, i):
  return 1.0 if hand == i else 0.0

def value(i):
  j = i // 6
  k = i % 6
  h = history[j][k // 3]
  if h == -1:
    return 0.0
  elif h == k % 3:
    return +2.0
  else:
    return -1.0

def action():
  for i in range(3):
    pred[i] = -thr[i]
    for j in range(6 * size):
      pred[i] += weight[i][j] * value(j)
    pred[i] = 1.0 / (1.0 + math.exp(-pred[i]))
  #g = max(0.0, pred[1] - pred[2])
  #c = g + max(0.0, pred[2] - pred[0])
  #p = c + max(0.0, pred[0] - pred[1])
  g = max(0.0, pred[1])
  c = g + max(0.0, pred[2])
  p = c + max(0.0, pred[0])
  if p == 0.0:
    return random.choice(['R', 'P', 'S'])
  r = p * random.random()
  if r < g:
    return 'R'
  elif r < c:
    return 'S'
  else:
    return 'P'

def result(mine, others):
  scale = 0.5 * eta / (6.0 * size + 1.0)
  for i in range(3):
    p = pred[i]
    df = scale * (ans(others, i) - p) / max(0.01, p * (1.0 - p))
    thr[i] -= df
    thr[i] *= decay
    for j in range(6 * size):
      weight[i][j] += value(j) * df
      weight[i][j] *= decay
  tmp = history[size - 1]
  for i in range(size - 1, 0, -1):
    history[i] = history[i - 1]
  history[0] = tmp
  history[0][0] = mine
  history[0][1] = others

if input == '':
  size = 7
  decay = 0.95
  eta = 0.26
  weight = [[random.gauss(0.0, 0.1 / size) for j in range(6 * size)] for i in range(3)]
  thr = [random.gauss(0.0, 0.1 / size) for i in range(3)]
  history = [[-1 for k in range(2)] for j in range(size)]
  pred = [0.0 for i in range(3)]
elif input == 'R':
  result(old_mine, 0)
elif input == 'S':
  result(old_mine, 1)
elif input == 'P':
  result(old_mine, 2)
output = action()
if output == 'R':
  old_mine = 0
elif output == 'S':
  old_mine = 1
elif output == 'P':
  old_mine = 2