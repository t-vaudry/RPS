'''
Barlow Q Odin

written 12/3/2013
'''
import random

if not input:
    #setup stage
    beats = {'P': 'S', 'S': 'R', 'R':'P'}
    my_history = ""                                             #historys are strings of previous choices
    opp_history = ""
    output = random.choice(['R','P','S'])
    hind_sight = 4
elif len(my_history) <= 4:  #random choice at beginning
    output = random.choice(['R','P','S'])                       
else:
    if beats[input] == output:                                  #won
        won = True
    else:                                                       #tie/loss
        if input == output:
            tie = True
        won = False
    my_history += output                                        #concat my previous choice to my history
    opp_history += input                                        #concat opponent's previous choice to their history
    predict = {'P': 0, 'S': 0, 'R': 0}
    counter = 1
    if len(my_history) < 75:                                    #only look at the last 100 matches for history
        begin = 0
    else:
        begin = len(my_history)-75
    while counter <= hind_sight:
        current_my_match = my_history[-counter:]                #my recent choices
        current_opp_match = opp_history[-counter:]              #opponent recent choices
        while begin <= len(my_history) - counter:               #step through history strings until loop reaches current length of recent choices
            if current_my_match == my_history[begin:begin+counter] and current_opp_match == opp_history[begin:begin+counter]:   #compare recent choices to previous history
                predict[opp_history[begin+counter+1]] += counter * (len(my_history) - begin) / len(my_history)    #if similar decision path is found, increment prediction based on amount of recent choices that were matched
    if predict['R'] > predict['S'] and predict['R'] > predict['P']:
        prediction = 'R'
    elif predict['S'] > predict['P'] and predict['S'] > predict['R']:
        prediction = 'S'
    else:
        prediction = 'P'
    if won:
        output = prediction
    elif not tie:
        output = beats[prediction]
    else:
        output = random.choice(['R','P','S'])