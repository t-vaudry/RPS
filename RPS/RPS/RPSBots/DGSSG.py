# Simple Guesser
# Uses the opponents most recent history in reacting to wins and losses
# to predict how they will change their input 
from collections import defaultdict
import random


if input == "":
    cscore = {'RR': 'T', 'PP': 'T', 'SS': 'T', 'PR': 'W', 'RS': 'W', 'SP': 'W','RP': 'L', 'SR': 'L', 'PS': 'L',}
    rotate = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 2, 'RS': 2, 'SP': 2,'RP': 1, 'SR': 1, 'PS': 1,}
    rps = ['R', 'P', 'S']
    rps_pos = {'R':0, 'P':1, 'S':2}
    rotate_str = 'RPSRPSRPS'
    hist = defaultdict(list)
    last_play = random.choice(rps)
    streak = ''
    output = random.choice(rps)
else:
    his_choice = rotate[last_play+input]
    result = cscore[input+output]
    #print("he: {}, us {}, result:{}".format(input, output, result))
    output = random.choice(rps)
    if streak:
        for i in xrange(len(streak)):
            hist[streak[:i]].append(his_choice)
        streak = result + streak[:7]
        for i in xrange(len(streak)):
            likely_choice = hist.get(streak[:i], None)
            if likely_choice is None:
                break
            else:
                #print("likely {}".format(likely_choice))
                pick = random.choice(likely_choice)
                output = rotate_str[rps_pos[input]+pick+1]
                #print ("based on streak of {} and likely {} choose {}".format(streak[:i], pick, output))
    else:
        streak = result
    last_play = input
#print("going with {}".format(output))