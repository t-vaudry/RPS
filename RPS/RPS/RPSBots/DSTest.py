if input == "":
  rr = rp = rs = 0
  pr = pp = ps = 0
  sr = sp = ss = 0
  output = "R"

elif input == "R":
  if rr > rp and rr > rs:
    output = "P"
  elif rp > rs:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rr += 1
  elif last == "P":
    pr += 1
  elif last == "S":
    sr += 1
  
elif input == "P":
  if pr > pp and pr > ps:
    output = "P"
  elif pp > ps:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rp += 1
  elif last == "P":
    pp += 1
  elif last == "S":
    sp += 1
  
elif input == "S":
  if sr > sp and sr > ss:
    output = "P"
  elif sp > ss:
    output = "S"
  else:
    output = "R"
  
  if last == "R":
    rs += 1
  elif last == "P":
    ps += 1
  elif last == "S":
    ss += 1

last = input