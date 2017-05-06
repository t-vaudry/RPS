import random, math

# first my, second opponent 
win={'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1}


if input == "":
  tmp  = 1
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev1 = {'R':tmp,'P':tmp,'S':tmp}
  
  output = random.choice(["R", "P", "S"])
  n = 0
  wins = 0
  loss = 0
  my_hist = []
  op_hist = []

else:
  op_hist.append(input)
  
  if n<5:

    output = random.choice(["R", "P", "S"])
  
  else:
    
    my_last = my_hist[n-1]
    
    my_l1 = my_hist[n-2]
    op_l1 = op_hist[n-2]
    
    if win[my_last+input]==1:
       lev1[my_l1][op_l1][my_last]+=1

    _,output=max((lev1[my_last][input][c],c) for c in 'SRP')    

if wins<loss:
      output = random.choice(["R", "P", "S"])

my_hist.append(output)
n+=1