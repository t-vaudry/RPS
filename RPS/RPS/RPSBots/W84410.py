import random, math

# the 410 comes from that choice
WIN  = 4
DRAW = 1
LOSS = 0

# first my, second opponent opponent
# give a certain ranking
ranks={'RR':DRAW,'PP':DRAW,'SS':DRAW,'PR':WIN,'RS':WIN,'SP':WIN,'RP':LOSS,'SR': LOSS,'PS':LOSS}

# default choice, unless the algorithm can't decide
# on something better

output = random.choice(["R", "P", "S"])

if input == "":

  tmp  = 0.6667
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev1 = {'R':tmp,'P':tmp,'S':tmp}
  
  n      = 0
  wins   = 0
  loss   = 0
  agefac = 0.6667
  
  my_hist = []
  op_hist = []

else:
  
  op_hist.append(input)
  
  if n>2:
  
    my_last = my_hist[n-1]
    my_l1 = my_hist[n-2]
    op_l1 = op_hist[n-2]
    score = ranks[my_last+input]
    lev1[my_l1][op_l1][my_last]+=score
    
    if score==WIN:
       wins+=1
    if score==LOSS:
       loss+=1
       
  if ((n>100) and (wins>loss)):
    
    dist = lev1[my_last][input]

    lev1[my_last][input]['R']=agefac*lev1[my_last][input]['R']
    lev1[my_last][input]['S']=agefac*lev1[my_last][input]['S']
    lev1[my_last][input]['P']=agefac*lev1[my_last][input]['P']

    w1 = dist['R']
    w2 = w1 + dist['S']
    w3 = w2 + dist['P']
    r = random.uniform(0.0,w3)

    if ((0<r) and (r<=w1)):
      output = 'R'
    if ((w1<r) and (r<=w2)):
      output = 'S'
    if ((w2<r) and (r<=w3)):
      output = 'P'

my_hist.append(output)
n+=1