n = 15
seed1 = 17
seed2 = 37
rvalue = 13
maxr = 124556789
his = ""
scores = {"RR":0, "SS":0, "PP":0, "RP":1, "PS":1, "SR":1, "PR":-1, "SP":-1, "RS":-1}
his_map = {}
vars = "RSP"
def r():
  global rvalue
  rvalue =  ((rvalue * seed1)+seed2)% maxr
  return vars[rvalue%3]

def best(s):
  a = s.count("R")
  b = s.count("S")
  c = s.count("P")
  if a > b and a > c:
    return "P"
  elif b > a and b > c:
    return "R"
  else:
    return "S"

def update():
  key = his[-n:-1]  
  lentry = his_map[key] if key in his_map else ""
  lentry+=his[-1]
  his_map[key]= lentry

if not input:
  score = 0
  prev_move = r()
elif len(input) < n:
  play = prev_move+input
  score += scores[play]
  #if score < -100:
  prev_move = r()
  #else:
  #  prev_move = input
  his+=input
else:
  last = his[-n::]
  if last in his_map:
    prev_move = best(his_map[last])
  else:
    prev_move = r()
  his+=input
  update()

output=prev_move