import random
SWITCH=25
response0 = {'R': 'R', 'P': 'P','S' : 'S'}
response1 = {'R': 'P', 'P': 'S','S' : 'R'}	
response2 = {'R': 'S', 'P': 'R','S' : 'P'}
############################
def highest(v):
    return random.choice([i for i in range(len(v)) if max(v) == v[i]])
#################################
if input == "": # initialize variables for the first round
    output=random.choice(['R','P','S'])
    round=0
    out=['','','','']
    strategy=[1,1,1,1]
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else: 
	if round >1 :
           for i in range(0,4):
                  string=out[i]+input  #My, His
                  strategy[i]+=result[string]

	if round<SWITCH:
		max_index=random.choice([0,1,2,3])
	else:
                max_index=highest(strategy)

        ##out contains responses based on various strategies
        out[0]=response0[input]
        out[1]=response1[input]	
        out[2]=response2[input]
        out[3]=random.choice(['R','P','S'])

        output=out[max_index]

	round+=1