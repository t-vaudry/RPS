#true power of stupid random
if not input:
  import time
  rvalue = int(time.time()*13)

n = 10
seed1 = 17
seed2 = 37

maxr = 127481957

vars = "RSP"
def r():
  global rvalue
  rvalue =  ((rvalue * seed1)+seed2)% maxr
  return vars[rvalue%3]


if not input:
  score = 0
prev_move = r()


output=prev_move