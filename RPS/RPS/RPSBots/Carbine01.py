#Carbine.py, an [hopefully] intelligent RPS prediction AI.
import random

ROCK = "R"
PAPER = "P"
SCISSOR = "S"
MAX_CYCLE = 10
MIN_CYCLE = 3

output = ""

if input == "":
   history = []
   weight = {}
   
   count = 0

   #change this whole mess to operate only on slices, building lists is
   #very unnecessary
for i in range(MAX_CYCLE):
   if (len(history) < (MIN_CYCLE - 1)) or (i < (MIN_CYCLE - 1)):
      continue
   else:
      testMoves = history[-(i+1):]
      weight = {ROCK:0, PAPER:0, SCISSOR:0}
      if len(testMoves) < MAX_CYCLE:
         testMoves.insert(i)
      else:
         break
      
      for j in range(len(history) - i):
         testCycle = history[j:j+i]

         #if it matches up, add the length of the chain
         if testMoves == testCycle:
            guess = history[j+i+1]

            weight[guess] = weight[guess] + i
            
r = weight.get(ROCK, 0)
p = weight.get(PAPER, 0)
s = weight.get(SCISSOR, 0)

if (r > p) and (r > s):
   output = ROCK
elif p > s:
   output = PAPER
else:
   output = SCISSOR

if output == "":
   output = random.choice([ROCK, PAPER, SCISSOR])