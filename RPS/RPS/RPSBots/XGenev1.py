'''
Barlow Q Odin

written 12/5/2013

added several different strategies
'''
import random
import operator

def new_mutant():
    ranked = sorted(xmen, key=lambda recruit: recruit[1])
    best = ranked[len(ranked)-1]
    second = ranked[len(ranked)-2]
    new_genes = []
    for gene_num in range(best[0]):
        if best[0][gene_num] == 0 and second[0][gene_num]:
            new_genes[gene_num] = random.choice(strats)
        elif best[0][gene_num] == 0:
            new_genes[gene_num] = second[gene_nume]
        elif second[0][gene_num] == 0:
            new_genes[gene_num] = best[gene_num]
        else:
            new_genes[gene_num] = random.choice([best[gene_num], second[gene_num]])
    new_mutant = (list(new_genes), 0, 0)                        #new mutant with inherited genes, zero mutant power, and age of zero
    xmen.append(new_mutant)
    
def apocalypse():
    for baggage in xmen:
        if baggage[2] == num_genes or baggage[1] < -10:         #mutant is too old or has lost too much power
            xmen.remove(baggage)
            new_mutant()
            
if not input:
    #setup stage
    beats = {'P': 'S', 'S': 'R', 'R':'P'}
    my_history = ""                                             #historys are strings of previous choices
    opp_history = ""
    hind_sight = 3
    size_of_xmen = 50
    num_genes = 30
    strats = ["pattern", "Lizard", "Spock", "Shotgun", "Jellyfish", "Same", "Ditto", "Dynamite", "Zombie", "Mummy"]
    strat_predict = {"pattern": 0, "Lizard": 0, "Spock": 0, "Shotgun": 0, "Jellyfish": 0, "Same": 0, "Ditto": 0, "Dynamite": 0, "Zombie": 0, "Mummy": 0}
        #Possible strategies:
        #pattern is pure pattern matching
        #Lizard is Anti-Rotation of pattern
        #Spock is Rotation of pattern
        #Shotgun is Anti-Rotation of opponent's previous
        #Jellyfish is Rotation of opponent's previous
        #Same is the same move of opponent's previous move
        #Ditto is copying my previous move
        #Dynamite is Random 
        #Zombie is Decayed Frequency Maximum
        #Mummy is Decayed Frequency Minimum
    frequency = {'P': 0, 'S': 0, 'R': 0}
    xmen = []
    for i in range(size_of_xmen):                               #create a new set of xmen, hopefully no one like Choir
        genes = []
        mutation_level = 0                                      #mutation level is the mutant's current strength
        age = 0                                                 #how long has the mutant been alive? hard to tell with Wolverine...
        for j in range(num_genes):                              #create a genome for this mutant randomly of specified length
            genes += random.choice(strats)
        mutant = (list(genes),mutation_level, age)
        xmen += tuple(mutant)                                   #give the mutant a uniform and add them to the roster of the xmen
    output = random.choice(['R','P','S'])
elif len(my_history) <= 3:                                      #random choice at beginning
    output = random.choice(['R','P','S'])
else:
    last_move = output
    last_opp_move = input
    if beats[input] == output:                                  #won
        won = True
    else:                                                       #tie/loss
        if output == input:
            tied = True
        else:
            tied = False
        won = False
    for hero in xmen:                                           #cycle through mutants
        age = hero[2]
        mutant_power = hero[0][age]                             #mutant power = current strat choice
        if beats[input] == strat_predict[mutant_power]:         #if mutant power would have won, add to their mutation level
            hero[1] += 2
        elif beats[strat_predict[mutant_power]] == input:       #if mutant power would have lost, subtract from the mutation level
            hero[1] -= 2
            hero[0][age] = 0                                    #strip the gene from the genome for later replacement if it reproduces
        else:
            hero[1] += .5                                       #mild increase of mutant power for a tie, but can keep gene
        hero[2] += 1                                            #age mutant by 1
    apocalypse()
    frequency[input] += 1
    for item in frequency:
        frequency[item] = 0.9 * frequency[item]                 #Decay all frequencies
    my_history += output                                        #concat my previous choice to my history
    opp_history += input                                        #concat opponent's previous choice to their history       
    predict = {'P': 0, 'S': 0, 'R': 0}
    counter = 1
    if len(my_history) < 50:                                    #only look at the last 50 matches for history
        begin = 0
    else:
        begin = len(my_history) - 50
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
    strat_predict["Lizard"] = beats[beats[prediction]]
    strat_predict["Spock"] = beats[prediction]
    strat_predict["Shotgun"] = beats[beats[last_opp_move]]
    strat_predict["Jellyfish"] = beats[last_opp_move]
    strat_predict["Same"] = last_opp_move
    strat_predict["Ditto"] = last_move
    strat_predict["Dynamite"] = random.choice(['R','P','S'])
    best = 0
    worst = 100000
    for item in frequency:
        if frequency[item] < worst:
            worst = frequency[item]
            strat_predict["Mummy"] = item
        if frequency[item] > best:
            best = frequency[item]
            strat_predict["Zombie"] = item
    rogue = max(xmen, key=itemgetter(1))                        #rogue takes on the powers of the best mutant
    rogue_age = rogue[2]
    chosen_power = rogue[0][rogue_age]                           #strategy gene at this mutant's age
    output = strat_predict[chosen_power]