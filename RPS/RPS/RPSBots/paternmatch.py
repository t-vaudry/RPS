import random
if input =="":
   predicted = -1
   val = {"R":0, "P":1, "S":2}
   sign ={0:"R", 1:"P", 2:"S"}
   patt = []
   resp = []
   output = random.choice(["R","P","S"])
if input != "":
   success = 0
   my = random.choice(["R","P","S"])
   total = 0
   move = input
   for i ,j in enumerate(patt):
       if j == move:
          total += 1.0
          predicted = sign[(val[patt[i]]+1)%3]
          if predicted == resp[i]:
              success += 1.0
              my = resp[i]
   patt += [move]
if input != "" and total > 0 and success/total > 0.5:
   resp +=[my]
   output = my
elif input != "":
   resp +=  [sign[(val[my]+1)%3]]
   output =  sign[(val[my]+1)%3]