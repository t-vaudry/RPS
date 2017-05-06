seed1 = 17
seed2 = 27
rvalue = 13
maxr = 65536

scores = {"RR":0, "SS":0, "PP":0, "RP":1, "PS":1, "SR":1, "PR":-1, "SP":-1, "RS":-1}
vars = "RSP"
def r():
  global rvalue
  rvalue =  ((rvalue * seed1)+seed2)% maxr
  return vars[rvalue%3]


if not input:
  score = 0
  prev_move = r()
else:
  play = prev_move+input
  score += scores[play]
  if score < -100:
    prev_move = r()
  else:
    prev_move = input

output=prev_move