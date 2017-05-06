import random
if input == "":
   moves = ["R","P","S"]
   play = {}
   for i in range(0,len(moves)):
      for j in range(0,len(moves)):
         play[moves[i]+moves[j]] = [0,0,0]
   my = [""]*1000
   op = [""]*1000
   output = my[0] = random.choice(["R","P","S"])
   i = 0

op[i] = input
if input == "R":
   play[op[i]+my[i-1]][0] += 1
   if my[i-1] == "R":
      if play["RR"][0] > play["RR"][1] and play["RR"][0] > play["RR"][2]:
         output = my[i]= "P"
      elif play["RR"][1] > play["RR"][2]:
         output = my[i] = "S"
      else:
         output = my[i] = "R"
   elif my[i-1] == "P":
      if play["RP"][0] > play["RP"][1] and play["RP"][0] > play["RP"][2]:
         output = my[i] = "P"
      elif play["RP"][1] > play["RP"][2]:
         output = my[i] = "S"
      else:
         output = my[i] = "R"
   else:
      if play["RS"][0] > play["RS"][1] and play["RS"][0] > play["RS"][2]:
         output = my[i] = "P"
      elif play["RS"][1] > play["RS"][2]:
         output = my[i] = "S"
      else:
         output = my[i] = "R"
elif input == "P":
   play[op[i]+my[i-1]][1] += 1
   if my[i-1] == "R":
      if play["PR"][0] > play["PR"][1] and play["PR"][0] > play["PR"][2]:
         output = my[i] = "P"
      elif play["PR"][1] > play["PR"][2]:
         output = my[i] = "S"
      else:
         output =my[i] = "R"
   elif my[i-1] == "P":
      if play["PP"][0] > play["PP"][1] and play["PP"][0] > play["PP"][2]:
         output = my[i] = "P"
      elif play["PP"][1] > play["PP"][2]:
         output =my[i] = "S"
      else:
         output =my[i] = "R"
   else:
      if play["PS"][0] > play["PS"][1] and play["PS"][0] > play["PS"][2]:
         output = "P"
      elif play["PS"][1] > play["PS"][2]:
         output =my[i] = "S"
      else:
         output =my[i] = "R"
elif input == "S":
   play[op[i]+my[i-1]][2] += 1
   if my[i-1] == "R":
      if play["SR"][0] > play["SR"][1] and play["SR"][0] > play["SR"][2]:
         output =my[i] = "P"
      elif play["SR"][1] > play["SR"][2]:
         output =my[i] = "S"
      else:
         output =my[i] = "R"
   elif my[i-1] == "P":
      if play["SP"][0] > play["SP"][1] and play["SP"][0] > play["SP"][2]:
         output =my[i] = "P"
      elif play["SP"][1] > play["SP"][2]:
         output =my[i] = "S"
      else:
         output =my[i] = "R"
   else:
      if play["SS"][0] > play["SS"][1] and play["SS"][0] > play["SS"][2]:
         output =my[i] = "P"
      elif play["SS"][1] > play["SS"][2]:
         output = my[i] = "S"
      else:
         output = my[i] = "R"   
i += 1