import random
SWITCH=25
#Strategies
response0 = {'R': 'R', 'P': 'P','S' : 'S'}
response1 = {'R': 'P', 'P': 'S','S' : 'R'}	
response2 = {'R': 'S', 'P': 'R','S' : 'P'}

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
    output=random.choice(['R','P','S'])
    round=0
    out=['','','','','','']
    strategy=[0.3,0.6,0.9,0.1,0.2,0.5]
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else: 
	if round >1 :
           for i in range(0,3):
                  string=out[i]+input  #My, His
                  strategy[i]+=result[string]
                  ##Next block keeps score between 0 and 3
                  if strategy[i] > 3:
                     strategy[i]=3
                  elif strategy[i]<0:
                     strategy[i]=0

	if round<SWITCH:
		max_index=random.choice([0,1,2,3,4,5])
	else:
                max_index=highest(strategy)

        ##out contains responses based on various strategies
        out[0]=response0[input]
        out[1]=response1[input]	
        out[2]=response2[input]
        out[3]=response0[output]
        out[4]=response1[output]
        out[5]=response2[output]

        output=out[max_index]

	round+=1