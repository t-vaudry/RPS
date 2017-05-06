from random import choice, randint

if input == "":
  count = [0,0,0] #rock paper scissor
  idx = {"R": 0, "P": 1, "S":2}
  c = ["R", "P", "S"]
  output = choice(c)
else:
  count[idx[input]]+=1
  tot = count[0]+count[1]+count[2]
  ans = randint(0, 101)
  if ans <= float(count[0])/tot*100:
    output = "P"
  elif ans <= float(count[1])/tot*100:
    output = "S"
  else:
    output = "R"