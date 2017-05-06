def thue_morse(v):
   if v == "R":
      return ["P","S"]
   if v == "P":
      return ["P","R", "S"]
   if v == "S":
      return ["R"]

def sequence():
   a = ["R"]
   for j in range(0,10):
      for i in range(int(len(a)/2),len(a)):
         a += thue_morse(a[i])
   return a
if input == "":
   seq = sequence()
   val = {"R":0, "P":1, "S":2}
   sign = {0:"R", 1:"P", 2:"S"}
   countseq = 0
   beat_prev = []
   countprev = 0
   i = 0
   j = 0
   v = []
if input == "R":
   beat_prev += ["P"]
if input == "P":
   beat_prev += ["S"]
if input == "S":
   beat_prev += ["R"]
output = seq[i]
if input != "" and sign[(val[input]+1)%3] == seq[i]:
   countseq += 1
if input != "" and sign[(val[input]+2)%3] == seq[i]:
   countseq -= 1
i += 1
if countseq < -10:
   output = beat_prev[j]
   j += 1