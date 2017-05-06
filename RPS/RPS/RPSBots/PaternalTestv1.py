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
    win_track = ""                                              #keeptrack of wins and losses
    output = random.choice(['R','P','S'])
    trickery = 0
    hind_sight = 5
elif len(my_history) % 10 == 0 or len(my_history) < hind_sight: #random choice every so often to keep pattern matchers guessing
    output = random.choice(['R','P','S'])                       #random at beginning to establish some footing and test opponent
else:
    my_history += output                                        #concat my previous choice to my history
    opp_history += input                                        #concat opponent's previous choice to their history
    predict = {'P': 0, 'S': 0, 'R': 0}
    prediction = ""
    if beats[input] == output:                                  #concat win/loss/tie to win_track
        win_track += "W"
        trickery = win_track[-10:].count('L') / 10              #reset trickery level a bit in case it was a misconception
    elif beats[output] == input:
        win_track += "L"                                        
        trickery += win_track[-5:].count('L') / 5               #opponent may have known the previous choice
    else:
        win_track += "T"
    counter = 1
    if len(my_history) < 50:                                    #only look at the last 50 matches for history
        begin = 0
    else:
        begin = len(my_history)-50
    while counter <= hind_sight:
        current_my_match = my_history[-counter:]                #my recent choices
        current_opp_match = opp_history[-counter:]              #opponent recent choices
        while begin <= len(my_history) - counter:               #step through history strings until loop reaches current length of recent choices
            if current_my_match == my_history[begin:begin+counter] and current_opp_match == opp_history[begin:begin+counter]:   #compare recent choices to previous history
                predict[opp_history[begin+counter+1]] += counter    #if similar decision path is found, increment prediction based on amount of recent choices that were matched
    if predict['R'] > predict['S'] and predict['R'] > predict['P']:
        prediction = 'R'
    elif predict['S'] > predict['P'] and predict['S'] > predict['R']:
        prediction = 'S'
    else:
        prediction = 'P'
    if trickery > .75:
        output = beats[prediction]                              #opponent is acting trickily, so expect a loss
    else:
        output = prediction