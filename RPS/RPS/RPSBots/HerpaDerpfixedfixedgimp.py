import random

if input == "":
    limit = 50
    count = 0
    rps = {'R':'S', 'P':'R', 'S':'P'}

    rdRate = .5
    faMinRate = 0
    faMaxRate = 0
    ccsRate = 0
    csRate = 0
    ccoRate = 0
    coRate = 0
    rpRate = 0

    rdOut = ""
    faMinOut = ""
    faMaxOut = ""
    ccsOut = ""
    csOut = ""
    ccRate = ""
    coOut = ""
    ccoOut = ""
    rpOut = ""

    fa = {'R':0, 'P':0, 'S':0}

elif count < limit and count > 2:

    def getResult(Out):
        if rps[Out] == input:
            return 1
        elif Out == input:
            return .5
        else:
            return 0

    faMinRate = ((faMinRate * count) + getResult(faMinOut))/count
    faMaxRate = ((faMaxRate * count) + getResult(faMaxOut))/count
    csRate = ((csRate * count) + getResult(csOut))/count
    ccsRate = ((ccsRate * count) + getResult(ccsOut))/count
    coRate = ((coRate * count) + getResult(coOut))/count
    ccoRate = ((ccoRate * count) + getResult(ccoOut))/count
    rpRate = ((rpRate * count) + getResult(rpOut))/count

elif count > 2:

    def getResult(Out):
        if rps[Out] == input:
            return 1
        elif Out == input:
            return .5
        else:
            return 0

    faMinRate = ((faRate * (limit - 1)) + getResult(faOut))/limit
    faMaxRate = ((faMaxRate * (limit - 1)) + getResult(faMaxOut))/limit
    csRate = ((csRate * (limit - 1)) + getResult(csOut))/limit
    ccsRate = ((ccsRate * (limit - 1)) + getResult(ccsOut))/count
    coRate = ((coRate * (limit - 1)) + getResult(coOut))/count
    ccoRate = ((ccoRate * (limit - 1)) + getResult(ccoOut))/count
    rpRate = ((rpRate * (limit - 1)) + getResult(rpOut))/limit

#Always run all the strats, to see how they perform, even when not used


if input != "":
    #Frequency Analysis Min - assume they will choose least chosen type
    #Frequency Analysis Max - assume they will choose most chosen type
    fa[input] = fa[input] + 1

    most = fa['R']
    faMinOut = 'R'
    faMaxOut = 'R'
    least = fa['R']
    for i in rps:
        if most < fa[i]:
            most  = fa[i]
            faMaxOut = i
        if least > fa[i]:
            least = fa[i]
            faMinOut = i
    
    #Counter Self - assume they will play what beat their last move
    csOut = rps[input]

    #Counter-Counter Self - assume they will play what is beaten by their last move
    ccsOut = rps[rps[input]]

    #Counter Opponent - assume they will play what beat opponent's last move
    coOut = rps[output]

    #Counter-Counter Opponent - assume the will play what is beaten by opponent's last move
    ccoOut = rps[rps[output]]

    #Repeat - assume they will play what they played last move
    rpOut = input

#Random
rdOut = random.choice(['R','P','S'])

#determine which strat to use
temp1 = [rdRate, faMinRate, faMaxRate, csRate, ccsRate, coRate, ccoRate, rpRate]
temp2 = [rdOut, faMinOut, faMaxOut, csOut, ccsOut, coOut, ccoOut, rpOut]

best = temp1[0]
output = temp2[0]

if count > limit:
    for i in range(1,len(temp1)):
        if best < temp1[i]:
            best = temp1[i]
            output = temp2[i]

++count
#clearly it will works THIS time