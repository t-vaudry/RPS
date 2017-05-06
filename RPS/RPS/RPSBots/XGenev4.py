'''
Barlow Q Odin

written 12/5/2013

change genetic to use only standard symbols rather than strategies
'''
import random
import operator

def new_mutant():
    ranked = sorted(xmen, key=lambda recruit: recruit[1])
    best = ranked[len(ranked)-1]
    second = ranked[len(ranked)-2]
    new_genes = []
    for gene_num in range(len(best[0])):
        if best[0][gene_num] == '0' and second[0][gene_num] == '0':
            new_genes.append(random.choice(choices))
        elif best[0][gene_num] == '0':
            new_genes.append(second[0][gene_num])
        elif second[0][gene_num] == '0':
            new_genes.append(best[0][gene_num])
        else:
            new_genes.append(random.choice([best[0][gene_num], second[0][gene_num]]))
    new_mutant = [new_genes, 0, 0]                        #new mutant with inherited genes, zero mutant power, and age of zero
    xmen.append(new_mutant)
    
def apocalypse():
    for baggage in xmen:
        if baggage[2] >= num_genes-1 or baggage[1] < -10:         #mutant is too old or has lost too much power
            xmen.remove(baggage)
            new_mutant()
            
def most_chosen():
    max = 0
    most = ''
    for choice in frequency:
        if frequency[choice] > max:
            most = choice
            max = frequency[choice]
    return most

if not input:
    #setup stage
    wins = 0
    total_games = 0
    beats = {'P': 'S', 'S': 'R', 'R':'P'}
    choices = ['P', 'S', 'R']
    frequency = {'P': 0, 'S': 0, 'R': 0}
    size_of_xmen = 10
    num_genes = 20
    xmen = []
    for i in range(size_of_xmen):                               #create a new set of xmen, hopefully no one like Choir
        genes = []
        mutation_level = 0                                      #mutation level is the mutant's current strength
        life = 0                                                 #how long has the mutant been alive? hard to tell with Wolverine...
        for j in range(num_genes+8):                              #create a genome for this mutant randomly of specified length
            genes.append(random.choice(choices))
        mutant = [genes, 0, 0]
        xmen.append(list(mutant))                                   #give the mutant a uniform and add them to the roster of the xmen
    output = random.choice(['R','P','S'])
    frequency[output] += 1
    total_games += 1
elif total_games <= 3:                                      #random choice at beginning
    output = random.choice(['R','P','S'])
    frequency[output] += 1
    total_games += 1
    if beats[input] == output:                                  #won
        won = True
    wins += 1
else:
    if beats[input] == output:                                  #won
        won = True
        wins += 1
    else:                                                       #tie/loss
        if output == input:
            tied = True
        else:
            tied = False
        won = False
    apocalypse()
    for hero in xmen:                                           #cycle through mutants
        age = hero[2]
        mutant_power = hero[0][age]                             #mutant power = current strat choice
        if beats[input] == mutant_power:         #if mutant power would have won, add to their mutation level
            hero[1] += 1
        elif beats[mutant_power] == input:       #if mutant power would have lost, subtract from the mutation level
            hero[1] -= 2
            hero[0][age] = '0'                                    #strip the gene from the genome for later replacement if it reproduces
        else:
            hero[1] += .5                                       #mild increase of mutant power for a tie, but can keep gene
        hero[2] += 1                                            #age mutant by 1
    rogue = max(xmen, key=operator.itemgetter(1))                        #rogue takes on the powers of the best mutant
    rogue_age = rogue[2]
    chosen_power = rogue[0][rogue_age]                           #strategy gene at this mutant's age
    if chosen_power == most_chosen():
        output = beats[chosen_power]
    else:
        output = chosen_power
    frequency[output] += 1