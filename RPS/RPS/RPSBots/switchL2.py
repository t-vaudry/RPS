import random, math

WIN  = 1
DRAW = 0
LOSS = -1

# first my, second opponent opponent
# give a certain ranking
ranks={'RR':DRAW,'PP':DRAW,'SS':DRAW,'PR':WIN,'RS':WIN,'SP':WIN,'RP':LOSS,'SR': 0,'PS':LOSS}

# default choice, unless the algorithm can't decide
# on something better
output = random.choice(["R", "P", "S"])

if input == "":

  tmp  = 1
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev1 = {'R':tmp,'P':tmp,'S':tmp}
  
  n    = 0
  wins = 0
  loss = 0
  
  my_hist = []
  op_hist = []

  strategy_score=[0,0,0]

  onemore={'S':'R','R':'P','P':'S'}

else:
  
  op_hist.append(input)

  strategy_score[0]=ranks[my_last+input]
  strategy_score[1]=ranks[onemore[my_last]+input]
  strategy_score[2]=ranks[ onemore[onemore[my_last]]+input]

  
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
       
  if ((n>10) and (wins>loss)):
    
    dist = lev1[my_last][input]
    w1 = dist['R']
    w2 = w1 + dist['S']
    w3 = w2 + dist['P']
    r = random.randint(1,w3)

    if ((0<r) and (r<=w1)):
      output = 'R'
    if ((w1<r) and (r<=w2)):
      output = 'S'
    if ((w2<r) and (r<=w3)):
      output = 'P'

my_last=output
if strategy_score[1]>strategy_score[0] or strategy_score[2]>strategy_score[0]:
  if strategy_score[1]>strategy_score[2]:
    output=onemore[my_last]
  else:
    output=onemore[onemore[my_last]]
my_hist.append(output)
n+=1