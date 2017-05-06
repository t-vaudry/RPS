if input == "":
   count = 0
   play = "R"
   nextplay = ""
   for i in range(0,10):
      for i in range(0,len(play)):
         if play[i] == "R":
            nextplay += "PS"
         if play[i] == "S":
            nextplay += "R"
         if play[i] == "P":
            nextplay += "PRS"
      play = nextplay
   output = "R"
if input != "":
   count += 1
   output = play[count]