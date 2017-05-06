"""
First simple (!) test app for rps contest...
microkernel, 2011
"""
def get_key_by_highest_value(var):
    var = map(lambda key: (key, var[key]), var) # format to tuple
    var.sort(key=lambda l:l[1], reverse=True)
    return var[0][0]
    
beat={"S":"R","P":"S","R":"P"}

if not input:
    used = dict()
    used["P"] = used["S"] = used["R"] = 0
    output = beat["S"] # most people use 'S' first
else:
    lastinput = input # (for me) so it is easier to think logic 
    poss = dict()
    poss["P"] = poss["S"] = poss["R"] = 1.0/3.0
    poss[lastinput] **= 2
    poss[get_key_by_highest_value(used)] += 0.1 

    output =  get_key_by_highest_value(poss)