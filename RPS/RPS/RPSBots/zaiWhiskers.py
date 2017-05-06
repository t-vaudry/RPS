# somewhat random

import math
import random

beats = {'R':'P', 'P':'S', 'S':'R'}

def randHand():
   return random.choice(['R', 'P', 'S'])

def response(mine, other):
   if mine == other:
      return other
   elif beats[mine] == other:
      return beats[other]
   else:
      return mine

# start of main code
if input is None or input == '':
   whiskerLength = 334
   myResponses = []
   
   output = randHand()
   lastHand = output
   handsPlayed = 1
else:
   index = handsPlayed % whiskerLength
   
   if handsPlayed < whiskerLength:
      myResponses.append(response(lastHand, input))
      output = randHand()
   else:
      output = myResponses[index]
      if index > 0:
         myResponses[index - 1] = response(lastHand, input)
      elif handsPlayed == whiskerLength:
         myResponses.append(response(lastHand, input))
   
   lastHand = output
   handsPlayed += 1