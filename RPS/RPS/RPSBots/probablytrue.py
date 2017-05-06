import random
if input == "":
   moves = ["R","P","S"]
   prob = [0.3,0.3,0.3]
   total = [0,0,0]
   output = random.choice(moves)

def select(prob,moves):
   v = random.random()*3
   k = 0
   m = 0
   while k < v:
      k += prob[m]
      m += 1
      if m == 3:
         m = 0
   output = moves[(m+1)%3]


if input == "R":
   total[0] += 1.0
   prob[0] =  total[0]/(total[0]+total[1]+total[2])
   select(prob,moves)
if input == "P":
   total[1] += 1.0
   prob[1] =  total[1]/(total[0]+total[1]+total[2])
   select(prob,moves)
if input == "S":
   total[2] += 1.0
   prob[2] =  total[2]/(total[0]+total[1]+total[2])
   select(prob,moves)