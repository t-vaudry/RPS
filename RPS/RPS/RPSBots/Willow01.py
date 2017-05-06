#pre=1.5  interval=1.0~11.5
import random
import math

def ans(hand, i):
  return 1.0 if hand == i else 0.0

def value(j, k):
  return +2.0 if history[j][k // 3] == k % 3 else -1.0

def action(pt):
  for i in range(3):
    pred[i] = -thr[i]
    for j in range(size):
      if history[j][1] == -1:
        break
      for k in range(6):
        pred[i] += weight[i][j][k] * value(j, k)
    pred[i] = 1.0 / (1.0 + math.exp(-pred[i]))
  sumpt = 0.0
  for j in range(14,0,-1):
   pt[j]=pt[j-1]
   sumpt+=pt[j]
  pt[0]=(((history[0][1]-history[0][0])+4)%3)-1
  # pt += win=1,lose=-1,drow=0
  sumpt+=pt[0]
  temp = 1.5# pre
  temp = (10.0 * sumpt)/15 + temp
  if temp < 1.0:
   temp = 1.0		
  g = math.exp(temp * (pred[1] - st * pred[2]))
  c = g + math.exp(temp * (pred[2] - st * pred[0]))
  p = c + math.exp(temp * (pred[0] - st * pred[1]))
  r = p * random.random()
  if r < g:
    return 'R',pt
  elif r < c:
    return 'S',pt
  else:
    return 'P',pt

def result(mine, others):
  scale = math.sqrt(0.5 * eta / (6.0 * size + 1.0))
  for i in range(3):
    df = scale * (ans(others, i) - pred[i])
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
  history[0][1] = others

if input == '':
  size = 10
  decay = 0.99
  eta = 0.25
  
  pt = [0.0 for j in range(15)]# sumpt volume
  st = 1.0
  weight = [[[random.gauss(0.0, 0.1) / size for k in range(6)] for j in range(size)] for i in range(3)]
  thr = [random.gauss(0.0, 0.1) / size for i in range(3)]
  #weight = [[[0.0 for k in range(6)] for j in range(size)] for i in range(3)]
  #thr = [0.0 for i in range(3)]
  history = [[-1 for k in range(2)] for j in range(size)]
  pred = [0.0 for i in range(3)]
elif input == 'R':
  result(old_mine, 0)
elif input == 'S':
  result(old_mine, 1)
elif input == 'P':
  result(old_mine, 2)
output,pt = action(pt)
if output == 'R':
  old_mine = 0
elif output == 'S':
  old_mine = 1
elif output == 'P':
  old_mine = 2