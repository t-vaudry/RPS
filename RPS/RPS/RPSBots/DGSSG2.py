# Simple Guesser
# Uses the opponents most recent history in reacting to wins and losses
# to predict how they will change their input
from collections import defaultdict, deque
import random

if input == "":
    cscore = {'RR': 'T', 'PP': 'T', 'SS': 'T', 'PR': 'W', 'RS': 'W', 'SP': 'W', 'RP': 'L', 'SR': 'L', 'PS': 'L'}
    score = {'W': -1, 'T': 0, 'L': 1}
    rotate = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 2, 'RS': 2, 'SP': 2, 'RP': 1, 'SR': 1, 'PS': 1}
    rps = ['R', 'P', 'S']
    rps_pos = {'R': 0, 'P': 1, 'S': 2}
    rotate_str = 'RPSRPSRPS'
    additional_rotate = 1  # the default amount to counter his move
    hist = defaultdict(list)
    last_play = random.choice(rps)
    streak = ''
    output = random.choice(rps)
    predict_scores = deque()

else:
    his_choice = rotate[last_play + input]
    result = cscore[input + output]
    predict_scores.append(score[result])
    if len(predict_scores) > 8:
        predict_scores.popleft()
        if sum(predict_scores) < -2:
            predict_scores.clear()
            additional_rotate = (additional_rotate + 1) % 3
            #print("setting rotate to {}".format(additional_rotate))

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
                output = rotate_str[rps_pos[input] + pick + additional_rotate]
                #print ("based on streak of {} and likely {} choose {}".format(streak[:i], pick, output))
    else:
        streak = result
    last_play = input
#print("going with {}".format(output))