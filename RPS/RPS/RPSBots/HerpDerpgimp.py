import random

if input == "":
    limit = 50
    count = 0
    rps = {'R':'S', 'P':'R', 'S':'R'}

    rdRate = .5
    faRate = 0
    csRate = 0
    coRate = 0
    rpRate = 0

    rdOut = ""
    faOut = ""
    csOut = ""
    coOut = ""
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

    faRate = ((faRate * count) + getResult(faOut))/count
    csRate = ((csRate * count) + getResult(csOut))/count
    coRate = ((coRate * count) + getResult(coOut))/count
    rpRate = ((rpRate * count) + getResult(rpOut))/count

elif count > 2:

    def getResult(Out):
        if rps[Out] == input:
            return 1
        elif Out == input:
            return .5
        else:
            return 0

    faRate = ((faRate * (limit - 1)) + getResult(faOut))/limit
    csRate = ((csRate * (limit - 1)) + getResult(csOut))/limit
    coRate = ((coRate * (limit - 1)) + getResult(coOut))/limit
    rpRate = ((rpRate * (limit - 1)) + getResult(rpOut))/limit

#Always run all the strats, to see how they perform, even when not used


if input != "":
#Frequency Analysis - assume they will choose least chosen type
    fa[input] = fa[input] + 1
    faTemp = fa.values()
    faTemp.sort()
    faOut = faTemp[0]

#Counter Self - assume they will play what beat their last move
    csOut = rps[input]

#Counter Opponent - assume they will play what beat opponent's last move
    coOut = rps[output]

#Repeat - assume they will play what they played last move
    rpOut = input

#Random
rdOut = random.choice(['R','P','S'])

#determine which strat to use
temp1 = [rdRate, faRate, csRate, coRate, rpRate]
temp2 = [rdOut, faOut, csOut, coOut, rpOut]

best = temp1[0]
output = temp2[0]
for i in range(1,len(temp1)):
    if best < temp1[i]:
        best = temp1[i]
        output = temp2[i]

if count < 50:
    best = temp1[0]
    output = temp2[0]