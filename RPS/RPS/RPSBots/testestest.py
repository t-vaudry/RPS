import re
import random
moves_my2 = []
moves_opp2 = []
output = ""
rockCount2 = 0
scissorsCount2 = 0
paperCount2 = 0
def player2(input):
    dict = {'R': '0', 'P': '1', 'S': '2'}
    dict2 = {'0': 'R', '1': 'P', '2': 'S'}
    global moves_my2
    global moves_opp2
    global output
    length = len(moves_my2)
    if length == 0:
        output = random.choice(("R", "P", "S"))
        return output
    else:
        moves_my2.append(dict[input])
        moves_opp2.append(dict[input])
        mymoves = "".join(moves_my2)
        oppmoves = "".join(moves_opp2)
        if length < 5: 
            sequence = oppmoves[-1]
            if oppmoves.count(sequence) == 1:
                output = random.choice(("R", "P", "S"))
        elif length >= 5 and length<=20:
            sequence = oppmoves[-3:]
            if oppmoves.count(sequence) ==1:
                sequence = oppmoves[-2:]
                if oppmoves.count(sequence) == 1:
                    sequence = oppmoves[-1]
                    if oppmoves.count(sequence)==1:
                        output = random.choice(("R", "P", "S"))
                        return output
        else:
            sequence = oppmoves[-6:]
            if oppmoves.count(sequence) <= 2:
                sequence = oppmoves[-5:]
                if oppmoves.count(sequence) <= 2:
                    sequence = oppmoves[-4:]
                    if oppmoves.count(sequence) <= 2:
                        sequence = oppmoves[-3:]
                        if oppmoves.count(sequence) <= 1:
                            sequence == oppmoves[-2:] 
                            if oppmoves.count(sequence) <= 1:
                                sequence == oppmoves[-1]
                                if oppmoves.count(sequence) <= 1:
                                    ouput = random.choice(("R", "P", "S"))
                                    return output
        indices = [(a.start(), a.end()) for a in list(re.finditer(sequence, oppmoves))]
        indices.pop()
        indices_length = len(indices)

        for i in range (indices_length):
            index1 = ("".join("".join(("".join(str(indices[i]).split(","))).split("(")).split(")"))).split(" ")[0]
            index2 = ("".join("".join(("".join(str(indices[i]).split(","))).split("(")).split(")"))).split(" ")[1]
            if oppmoves.count(sequence) != 1:
                if oppmoves[int(index2)+1] == "0":
                    global rockCount2
                    rockCount2+=1
                elif oppmoves[int(index2)] == "1":
                    global paperCount2
                    paperCount2+=1
                elif oppmoves[int(index2)] == "2":
                    global scissorsCount2
                    scissorsCount2+=1
            else:
                return random.choice(("R", "P", "S"))
        totalCount2 = rockCount2+paperCount2+scissorsCount2
        rockPercentage2 = float(rockCount2)/totalCount2
        paperPercentage2=float(paperCount2)/totalCount2
        scissorsPercentage2=float(scissorsCount2)/totalCount2
        random_float = random.random()
        paperPercentage2 = rockPercentage2+paperPercentage2
        scissorsPercentage2 = rockPercentage2+paperPercentage2+scissorsPercentage2
        rockCount2=0
        paperCount2=0
        scissorsCount2=0
        if (rockPercentage2-random_float) >= 0:
            ouput = "P"
            return ouput
        if (paperPercentage2-random_float) >= 0:
            ouptut = "S"
            return output
        if (scissorsPercentage2-random_float) >=0:
            ouput = "R"
            return ouput
player2(input)