# pattern which stores all level 3-backward strategies
import random, math

# parameters
WIN  = 3
DRAW = 1
LOSS = 0

# first my, second opponent opponent
# give a certain ranking
ranks={'RR':DRAW,'PP':DRAW,'SS':DRAW,'PR':WIN,'RS':WIN,'SP':WIN,'RP':LOSS,'SR': 0,'PS':LOSS}

# default choice, unless the algorith can't decide
# on something better
output = random.choice(["R", "P", "S"])

if input == "":
  
  # should work always
  tmp  = 1
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev1 = tmp
  
  # might work
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev2 = tmp

  # only if lev3 is sparse
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev3 = tmp

  n    = 0
  wins = 0
  loss = 0
  
  my_hist = []
  op_hist = []

else:
  
  op_hist.append(input)
  
  if n>4:
  
    my_last = my_hist[n-1]
    op_last = input
    
    my_l1 = my_hist[n-2]
    op_l1 = op_hist[n-2]
    my_l2 = my_hist[n-3]
    op_l2 = op_hist[n-3]
    my_l3 = my_hist[n-4]
    op_l3 = op_hist[n-4]
      
    score = ranks[my_last+op_last]
    
    lev1[my_l1][op_l1][my_last]+=score
    lev2[my_l2][op_l2][my_l1][op_l1][my_last]+=score
    lev3[my_l3][op_l3][my_l2][op_l2][my_l1][op_l1][my_last]+=score
    
    if score==WIN:
       wins+=1
    if score==LOSS:
       loss+=1
       
  if ((n>10) and (wins>=loss)):
    
    dist_l1=lev1[my_last][op_last]
    dist_l2=lev2[my_l1][op_l1][my_last][op_last]
    dist_l3=lev2[my_l1][op_l1][my_last][op_last]
    
    dist = {'R':1,'P':1,'S':1}
    
    if (dist_l1['R']+dist_l1['S']+dist_l1['P'])>10:
       dist = dist_l1
    if (dist_l2['R']+dist_l2['S']+dist_l2['P'])>10:
       dist = dist_l2
    if (dist_l3['R']+dist_l3['S']+dist_l3['P'])>10:
       dist = dist_l3
       
    
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

my_hist.append(output)
n+=1