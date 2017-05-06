import random
if(1):
    if input =="":
        #initialize parameters
        his1 =""
        your_move =""
        #my_move =""
        num_p = 13 
        predictors = [random.choice("RPS")]*num_p 
        predictors_score = [4]*num_p
        output = random.choice("RPS")
        beat = { "P":"S","R":"P","S":"R"}
        not_lose = { "P":"SSP", "R":"PPR","S":"RRS"}
        temp1 = { "PP":"1","PR":"2","PS":"3",
                "RP":"4","RR":"5","RS":"6",
                "SP":"7","SR":"8","SS":"9"}
        temp2 = { "1":"PP","2":"PR","3":"PS",
                "4":"RP","5":"RR","6":"RS",
                "7":"SP","8":"SR","9":"SS"}
        who_win = { "PP": 0, "PR": 1, "PS":-1,  #1 = first player win
                    "RP": -1, "RR":0, "RS":1,   #-1 = second player win
                    "SP": 1, "SR":-1, "SS":0}   #0 = draw
        #markov init
        limit = [10,20,60,120]
    else:
        #update predictor score
        for i in range(num_p):
            #First selection
            #predictors_score[i] *=0.8
            predictors_score[i] += (input==predictors[i])*4
            predictors_score[i] -= (input==beat[beat[predictors[i]]])*predictors_score[i]

        #update predictor
        predictors[0] = random.choice("RPS")
        his1 += temp1[(output+input)] 
        your_move += input
        #my_move += output
        # Markov model
        for i in limit:
            temp =""
            temp_len = len(his1) # number of round
            search = temp1[(output+input)] #last round
            for start in range(2, min(i, temp_len) ):
                if search == his1[temp_len-start]:
                    temp+=his1[temp_len-start+1]
            if(temp==""): 
                predictors[1+limit.index(i)] = random.choice("RPS")
                predictors[9+limit.index(i)] = random.choice("RPS")
            else:
                collectI = {"P":0,"R":0,"S":0}
                collectR = {"P":0,"R":0,"S":0}
                for sdf in temp:    
                    collectI[temp2[sdf][1]]+=1
                    next_move = temp2[sdf]
                    if(who_win[next_move]==-1):
                        collectR[temp2[sdf][1]]+=3
                    elif(who_win[next_move]==0):
                        collectR[temp2[sdf][1]]+=1
                    elif(who_win[next_move]==1):
                        collectR[beat[temp2[sdf][0]]]+=1
                max1 = -1
                max2 = -1
                for key in collectI:
                    if(collectI[key]>max1):
                        max1 = collectI[key]
                        p3 = key
                for key in collectR:
                    if(collectR[key]>max2):
                        max2 = collectR[key]
                        p4 = key
                predictors[1+limit.index(i)] = p3
                predictors[9+limit.index(i)] = p4
                
        for i in limit:
            temp =""
            temp_len = len(your_move) 
            search = input
            collectK = { "P":0,"R":0,"S":0}
            for start in range(2, min(i, temp_len) ):
                if search == your_move[temp_len-start]:
                    collectK[your_move[temp_len-start+1]]+=1     
            if(temp==""):
                predictors[5+limit.index(i)] = random.choice("RPS")
            else:
                max3 = -1
                for key in collectK:
                    if(collectK[key]>max3):
                        max3 = collectK[key]
                        p5 = key
                predictors[5+limit.index(i)] = p5

        #choose the predictor
        predict = predictors[predictors_score.index(max(predictors_score))]
        output = random.choice(not_lose[predict])