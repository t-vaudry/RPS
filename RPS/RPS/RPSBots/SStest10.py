import random

def print2 (s):
#    print s
    return

def calcWinLose():
    global win_count
    global lose_count
    global draw_count

    win_count=0
    lose_count=0
    draw_count=0


    for round in choices.split(","):
        if round=="SP" or round=="RS" or round=="PR":
            win_count+=1
        elif round[:1]==round[-1:]:
            draw_count+=1
        else:
            lose_count+=1

    return

if input == "":
    win_count=0
    lose_count=0
    draw_count=0

    my_choice=[]
    his_choice=[]
    counter=1
    choices=""

    #output = random.choice(["R","P","S"])
    output = "S"
else:
    calcWinLose()
    counter+=1
    choices+=input+','

#    output = "R"
    output = random.choice(["P","S","R"])
    if win_count<lose_count:
        pattern_len=3*10
        last_pattern=choices[-pattern_len:]
        print2("last="+last_pattern)
        pos = choices[:-pattern_len].find(last_pattern)
        print2("pos="+str(pos))
        if pos!=-1:
            expectation=choices[pos+pattern_len:pos+pattern_len+1]
            expectation_his=choices[pos+pattern_len+1:pos+pattern_len+2]

            print2("expectation="+expectation)
            print2("expectation_his="+expectation_his)

            if expectation == "R":
                output = random.choice(["P","S"])
            if expectation == "P":
                output = random.choice(["R","S"])
            if expectation == "S":
                output = random.choice(["R","P"])

            if expectation_his == "R":
                output = "P"
            if expectation_his == "S":
                output = "R"
            if expectation_his == "P":
                output = "S"

            new_pattern=last_pattern+output
            pos_new = choices[:-pattern_len].find(new_pattern)
            if (pos_new!=-1):
                output = random.choice(["R","P","S"])
                pass

        print2("output="+output)

#    output = random.choice(["P","S","R"])

choices+=output
#choices+=str(counter)

my_choice.append(output)
his_choice.append(input)