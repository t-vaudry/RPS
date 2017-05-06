import random
if(1):
    if input =="":
        #initialize parameters
        his1 =""
        your_move =""
        my_move =""
        num_p = 7 
        predictors = [random.choice("RPS")]*num_p 
        predictors_score = [4]*num_p
        output = random.choice("RPS")
        beat = { "P":"S","R":"P","S":"R"}
        temp1 = { "PP":"1","PR":"2","PS":"3",
                "RP":"4","RR":"5","RS":"6",
                "SP":"7","SR":"8","SS":"9"}
        temp2 = { "1":"PP","2":"PR","3":"PS",
                "4":"RP","5":"RR","6":"RS",
                "7":"SP","8":"SR","9":"SS"}
        #markov init
        limit = [20,60,120,500]
        order = [1,2,3]
    else:
        #update predictor score
        for i in range(num_p):
            #First selection
            predictors_score[i] += (input==predictors[i])*4
            predictors_score[i] -= (input==beat[beat[predictors[i]]])*predictors_score[i]

        #update predictor
        predictors[0] = random.choice("RPS")
        his1 += temp1[(output+input)]
        your_move += input
        my_move += output
        for length in range( min(25, len(his1)-1),0,-1):
            search = his1[-length:]
            idx = his1.rfind(search,0,-1)
            if idx !=-1:
                answer = his1[idx+length]
                expect = temp2[answer][1]
                predictors[1] = expect
                predictors[2] = beat[expect]
                predictors[3] = beat[beat[expect]]
                expect = temp2[answer][0]
                predictors[4] = expect
                predictors[5] = beat[expect]
                predictors[6] = beat[beat[expect]]
                break
            else:
                predictors[1] = random.choice("RPS")
                predictors[2] = random.choice("RPS")
                     
        
        #choose the predictor
        predict = predictors[predictors_score.index(max(predictors_score))]

        output = beat[predict]