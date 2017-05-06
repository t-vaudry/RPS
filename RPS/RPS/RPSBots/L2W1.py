# pattern which stores all level 2-backward strategies
import random, math

# parameters
sWIN  = 2
sTIE  = 2
sLOSS = 0

WIN  = 2
TIE  = 1
LOSS = 0


# first my, second opponent opponent
# give a certain ranking

ranks={'RR':TIE,'PP':TIE,'SS':TIE,'PR':WIN,'RS':WIN,'SP':WIN,'RP':LOSS,'SR': LOSS,'PS':LOSS}
scores={'RR':sTIE,'PP':sTIE,'SS':sTIE,'PR':sWIN,'RS':sWIN,'SP':sWIN,'RP':sLOSS,'SR': sLOSS,'PS':sLOSS}

# default choice, unless the algorith can't decide
# on something better
output = random.choice(["R", "P", "S"])

if input == "":

  tmp  = 1
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev1 = tmp
  
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  tmp  = {'R':tmp,'P':tmp,'S':tmp}
  lev2 = tmp
  
  n    = 0
  wins = 0
  loss = 0
  
  my_hist = []
  op_hist = []

else:
  
  op_hist.append(input)
  
  if n>3:
  
    my_last = my_hist[n-1]
    op_last = input
    
    my_l1 = my_hist[n-2]
    op_l1 = op_hist[n-2]
    my_l2 = my_hist[n-3]
    op_l2 = op_hist[n-3]
    
    score  = scores[my_last+op_last]
    decide = ranks[my_last+op_last]

    lev1[my_l1][op_l1][my_last]+=score
    lev2[my_l2][op_l2][my_l1][op_l1][my_last]+=score
    
    if decide==WIN:
       wins+=1
    if decide==LOSS:
       loss+=1
       
  if ((n>10) and (wins>loss)):
    
    dist_l2=lev2[my_l1][op_l1][my_last][op_last]
    dist_l1=lev1[my_last][op_last]

# check out chances to win with a particular strategy

    value_l1 = (1.0*dist_l1['S'])/(dist_l1['P']+dist_l1['R'])+(1.0*dist_l1['R'])/(dist_l1['P']+dist_l1['S'])+(1.0*dist_l1['P'])/(dist_l1['S']+dist_l1['R'])

    value_l2 = (1.0*dist_l2['S'])/(dist_l2['P']+dist_l2['R'])+(1.0*dist_l2['R'])/(dist_l2['P']+dist_l2['S'])+(1.0*dist_l2['P'])/(dist_l2['S']+dist_l2['R'])

    r = random.uniform(0,value_l1+value_l2)

    if (r<=value_l1):
         dist = dist_l1
    else:
         dist = dist_l2

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