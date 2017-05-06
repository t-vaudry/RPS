import random
SWITCH=25
#Strategies
response0 = {'R': 'S', 'P': 'R','S' : 'P'}
response1 = {'R': 'R', 'P': 'P','S' : 'S'}	
response2 = {'R': 'P', 'P': 'S','S' : 'R'}

############################
def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])
##############################
def most_common(l):
    max = 0
    maxitem = None
    for x in set(l):
        count =  l.count(x)
        if count > max:
            max = count
            maxitem = x
    return maxitem
#################################
if input == "": # initialize variables for the first round
    history=''
    output=random.choice(['R','P','S'])
    round=0
    out=['','','','','','']
    prediction=['R','P','S']
    strategy=[1,1,1]
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else:
        history += input
	if round >1 :
           for i in range(0,3):
                  string=out[i]+input  #My, His
                  strategy[i]+=result[string]

        #What's he going to play next?
        prediction[0] = most_common(history)#Max so far
        prediction[1] = random.choice(['R','P','S'])#Random
        sett=['R','P','S']
        sett.remove(input) 
        prediction[2]=random.choice(sett)         #Random of pair excluding last played by him
      
        pred=random.choice(prediction)
         
        ##out contains responses based on various strategies
        out[0] = response0[pred]
        out[1]=response1[pred]	
        out[2]=response2[pred]

	if round<SWITCH:
		output=random.choice(['R','P','S'])
	else:   
                output=out[highest(strategy)]

	round+=1