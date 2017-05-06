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
if input == "": # initialize variables for the first round
    output=random.choice(['R','P','S'])
    round=0
    out=['','','']
    result={'RR':0,'PP':0,'SS':0,'RP':-1,'RS':1,'PR':+1,'PS':-1,'SR':-1,'SP':+1}
else: 
	if round<SWITCH:
		max_index=random.choice([0,1,2])
	else:
                string=output+input  #My, His
                if  result[string] < 0:
                      temp=[0,1,2]
                      temp.remove(max_index)
                      max_index=random.choice(temp)

        ##out contains responses based on various strategies
        out[0]=response0[input]
        out[1]=response1[input]	
        out[2]=response2[input]

        output=out[max_index]

	round+=1