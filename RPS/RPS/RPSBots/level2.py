import random

def win(a, b):
  if a == b:
    return 0
  if a == "R":
    if b == "S":
      return 1
    else:
      return -1
  elif a == "S":
    if b == "P":
      return 1
    else:
      return -1
  elif a == "P":
    if b == "R":
      return 1
    else:
      return -1

levels = ["RPS", "PSR", "SRP"]
    
if input == "":
  seq_in = []
  seq_out = []
  winner = []
  levelscores = [0, 0, 0]
  output = random.choice(["R", "P", "S"])
  seq_out.append(output)
  level = 1
  matches = 0
else:
  seq_in.append(input)
  winner.append(win(seq_out[-1], seq_in[-1]))
  levelscores[level] += sum(winner)
  statistics = [len(filter(lambda x:x==b, seq_in)) for b in "RPS"]

  if matches%4 == 0:
    level = (levelscores.index(min(levelscores)) + 1)%3
    winner = []

  matches += 1

  leveldata = levels[level]
  pool = [leveldata[0]] * statistics[0] + [leveldata[1]] * statistics[1] + [leveldata[2]] * statistics[2]
  output = random.choice(pool)
  seq_out.append(output)