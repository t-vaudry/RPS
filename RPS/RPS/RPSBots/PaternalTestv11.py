'''
Barlow Q Odin

written 12/4/2013

added several different strategies
'''
import random

if not input:
    #setup stage
    beats = {'P': 'S', 'S': 'R', 'R':'P'}
    my_history = ""                                             #historys are strings of previous choices
    opp_history = ""
    hind_sight = 6
    strats = ["pattern", "Lizard", "Spock", "Shotgun", "Jellyfish", "Dynamite", "Zombie"]
    strat_stat = {"pattern": 0, "Lizard": 0, "Spock": 0, "Shotgun": 0, "Jellyfish": 0, "Dynamite": 0, "Zombie": 0}
    strat_predict = {"pattern": "", "Lizard": "", "Spock": "", "Shotgun": "", "Jellyfish": "", "Dynamite": "", "Zombie": ""}
        #Possible strategies:
        #pattern is pure pattern matching
        #Lizard is Anti-Rotation of my previous
        #Spock is Rotation of my previous
        #Shotgun is Anti-Rotation of opponent's previous
        #Jellyfish is Rotation of opponent's previous
        #Dynamite is Random 
        #Zombie is Decayed Frequency Count
    frequency = {'P': 0, 'S': 0, 'R': 0}
    current_strat = random.choice(strats)
    output = random.choice(['R','P','S'])
elif len(my_history) <= 3:  #random choice at beginning
    output = random.choice(['R','P','S'])
else:
    last_move = output
    last_opp_move = input
    for item in strat_predict:
        if input == strat_predict[item]:
            strat_stat[item] += 1
    if beats[input] == output:                                  #won
        won = True
    else:                                                       #tie/loss
        won = False
    if won:
        strat_stat[current_strat] += 1
    else:
        strat_stat[current_strat] = 0
        new_strat_cost = 0
        for possible in strat_stat:
            if strat_stat[possible] >= new_strat_cost:
                current_strat = possible
                new_strat_cost = strat_stat[possible]
    if len(my_history) % 17 == 0:
        current_strat = "Dynamite"   
    for item in strat_stat:
        strat_stat[item] = 0.9 * strat_stat[item]              #Decay all strategy's score
    frequency[input] += 1
    for item in frequency:
        frequency[item] = 0.9 * frequency[item]                #Decay all frequencies
    my_history += output                                        #concat my previous choice to my history
    opp_history += input                                        #concat opponent's previous choice to their history
    predict = {'P': 0, 'S': 0, 'R': 0}
    counter = 1
    if len(my_history) < 100:                                    #only look at the last 500 matches for history
        begin = 0
    else:
        begin = len(my_history) - 100
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
    strat_predict["pattern"] = prediction                       #record predictions from each strategy
    strat_predict["Lizard"] = beats[beats[last_move]]
    strat_predict["Spock"] = beats[last_move]
    strat_predict["Shotgun"] = beats[beats[last_opp_move]]
    strat_predict["Jellyfish"] = beats[last_opp_move]
    strat_predict["Dynamite"] = random.choice(['R','P','S'])
    best = 0
    for item in frequency:
        if frequency[item] > best:
            best = frequency[item]
            strat_predict["Zombie"] = beats[item]
    if current_strat == "pattern":
        output = strat_predict["pattern"]
    elif current_strat == "Lizard":
        output = strat_predict["Lizard"]
    elif current_strat == "Spock":
        output = strat_predict["Spock"]
    elif current_strat == "Shotgun":
        output = strat_predict["Shotgun"]
    elif current_strat == "Jellyfish":
        output = strat_predict["Jellyfish"]
    elif current_strat == "Dynamite":
        output = strat_predict["Dynamite"]
    else:
        output = strat_predict["Zombie"]