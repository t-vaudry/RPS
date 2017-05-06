import random
import math

def ans(hand, i):
  return 1.0 if hand == i else 0.0

def value(j, k):
  return +2.0 if history[j][k // 3] == k % 3 else -1.0

def action():
  for i in range(3):
    pred[i] = -thr[i]
    for j in range(size):
      if history[j][1] == -1:
        break
      for k in range(6):
        pred[i] += weight[i][j][k] * value(j, k)
    pred[i] = 1.0 / (1.0 + math.exp(-pred[i]))
  g = max(0.0, pred[1] - pred[2])
  c = g + max(0.0, pred[2] - pred[0])
  p = c + max(0.0, pred[0] - pred[1])
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
  p = 0.0
  q = 0.0
  for i in range(3):
    r = ans(others, i) - pred[i]
    s = r * pred[i] * (1.0 - pred[i])
    p += r * r
    q += s * s
  scale = eta * p / max(0.001, q) / (12.0 * size + 2.0)
  for i in range(3):
    df = scale * (ans(others, i) - pred[i]) * pred[i] * (1.0 - pred[i])
    thr[i] *= decay
    thr[i] -= df
    for j in range(size):
      if history[j][0] == -1:
        break
      for k in range(6):
        weight[i][j][k] *= decay
        weight[i][j][k] += value(j, k) * df
  tmp = history[size - 1]
  for i in range(size - 1, 0, -1):
    history[i] = history[i - 1]
  history[0] = tmp
  history[0][0] = mine
  history[0][0] = others

if input == '':
  size = 4
  decay = 0.9
  eta = 0.2
  weight = [[[random.gauss(0.0, 0.1) / size for k in range(6)] for j in range(size)] for i in range(3)]
  thr = [random.gauss(0.0, 0.1) / size for i in range(3)]
  history = [[-1 for k in range(2)] for j in range(size)]
  pred = [0.0 for i in range(3)]
  old_mine = -1
if input == 'R':
  result(old_mine, 0)
elif input == 'S':
  result(old_mine, 1)
elif input == 'P':
  result(old_mine, 2)
output = action()
old_mine = output