import random
if input == "":
   history = ""
   longest_substr = 0
   output = random.choice(["R","P","S"])
else:
   history += input
   output = do_history()
   if len(history) > 2 :
      output = do_history()
   else:
      output = random.choice(["R","P","S"])

def do_history():
   next = "R"
   if (len(history) > 10):
      max_len = 10
   else:
      max_len = len(history)
   for i in range(1,max_len) :
      substr = history[-i:]
      if history.count(substr)> 1:
         next = history[history.index(substr)+len(substr)]
   return next