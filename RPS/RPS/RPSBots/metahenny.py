#MetaHenny
import random 
decay=.95
def our_output(num):
    if num==0:
        return "R"
    elif num==1:
        return "P"
    elif num==2:
        return "S"

def read_input(char):
    if char=="R":
        return 0
    if char=="P":
        return 1
    if char=="S":
        return 2

if input == "":
    opp_moves = ""
    our_moves = ""
    allmoves = ""
    score = [0]*9
    score[0] = 10 #Bias us towards classical Henny
    Henny = [random.randint(0,2) for x in range(9)]
    win = 0
    decayedwin = 0
    quit = False
    
else: 
    move = read_input(input)
    opp_moves = opp_moves+str(move)
    allmoves = allmoves+str(move)
    
    decayedwin = decayedwin*.9 
    if (attack-move)%3==1:
        win+=1
        decayedwin+=1
    elif (attack-move)%3==2:
        win -= 1
        decayedwin+=1
    #scores the previous round
    score = [x*decay for x in score]
    scoring = [move==x for x in Henny]
    for j in range(9):
        score[j] = score[j]+scoring[j]
    max_value = max(score)
    max_index = score.index(max_value)

    
    #creates the new moves
    Henny[0] = int(random.choice(opp_moves))
    Henny[1] = int(random.choice(our_moves))
    Henny[2] = int(random.choice(allmoves))
    for i in range(3):
        Henny[i+3] = (Henny[i]+1)%3
        Henny[i+6] = (Henny[i]+2)%3



if len(opp_moves)>=50 and len(opp_moves)<200:
    decay-=.001

#If we are losing, cut our losses    
if win<=-50:
    quit=True
#If we won in the past but are losing now (eg, playing against a slower, better, algorithm), quit while ahead.
if win>5 and decayedwin<=-5:
    quit=False

if len(opp_moves)<=random.randint(3,25) or max_value<1.7 or quit:
    attack = random.randint(0,2)
else: 
    attack = (Henny[max_index]+1)%3

our_moves += str(attack)
allmoves += str(attack)
output = our_output(attack) 
output