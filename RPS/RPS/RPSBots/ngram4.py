from __future__ import division

import collections
import copy
import random

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

beat = {
    'R': 'P',
    'P': 'S',
    'S': 'R'
}

n_gram_length = 8
tot_rocks = 1
tot_papers = 1
tot_scissors = 1

move_history = []
their_move_history = []
last_output = None
output = ROCK

NGRAM_LENGTH=10

def extend_history(last_pair):
    '''
    Update any data structures we are maintaining based on the move history
    '''    
    
    move_history.append(last_pair)
    their_move_history.append(input)
    
    global tot_rocks
    global tot_papers
    global tot_scissors
    
    if input == ROCK:
        tot_rocks += 1
    elif input == PAPER:
        tot_papers += 1
    else:
        tot_scissors += 1
        
        
def generate_ngram_odds(history, i):
    
    # 1-length ngrams are nonsensical
    if i < 2:
        return None
    
    # As are odd-length ngrams
    if i % 2 != 0:
        return None
    
    seq, final = history[-i:-1], history[-1]
    
    chunks = []
    copy_history = copy.copy(history)
    while(len(copy_history) > i):
        chunks.append(tuple(copy_history[:i]))
        copy_history.pop(0)
        
    outcomes = []
    for chunk in chunks:
        cSeq, cFinal = chunk[:-1], chunk[-1]
        
        # Only search for chunks which match the current next move
        if seq != cSeq:
            continue
        
        outcomes.append(final)
        
    if len(outcomes) == 0:
        return None
        
    counter = collections.Counter(outcomes)
    most_common, count = counter.most_common(1)
    ratio = count / len(outcomes)
    
    if ratio > (1/3):
        return (most_common, ratio)     
        
def generate_moves_and_likelihoods():
    
    choices = []
    
    for i in range(NGRAM_LENGTH):
        choice = generate_ngram_odds(move_history, i)
        if choice:
            choices.append(choice)
        
        choice = generate_ngram_odds(their_move_history, i)
        if choice:
            choices.append(choice)
        
    total_moves = tot_rocks + tot_papers + tot_scissors
    rock_ratio = tot_rocks / total_moves
    paper_ratio = tot_papers / total_moves
    scissor_ratio = tot_scissors / total_moves
    
    choices.append(("R", rock_ratio))
    choices.append(("P", paper_ratio))
    choices.append(("S", scissor_ratio))

#    print choices    
    return choices
    
def get_likely_move():
    
    choices = generate_moves_and_likelihoods()
    
    max_move = None
    max_likelihood = 0
    for move, likelihood in choices:
        if likelihood > max_likelihood:
            max_move = move
            max_likelihood = likelihood
             
    # Only choose a nonrandom output if the odds are greater than a random
    # choice would allow
    
    if max_likelihood > (1/3):
        return max_move

def weighted_rand_move():
    
    total_moves = tot_rocks + tot_papers + tot_scissors
    rnum = random.random()
    
    rock_ratio = tot_rocks / total_moves
    paper_ratio = ((tot_rocks + tot_papers) / total_moves)
    
    if rnum < rock_ratio:
        return ROCK
    
    elif rnum < paper_ratio:
        return PAPER
    else:
        return SCISSORS

if not input:
    move_list = []
    output = random.choice(["R", "P", "S"])
    last_output = output

else:

    last_pair = (input, last_output)    
    extend_history(last_pair)

    # Get a likely move if one is available
    expected_opp_move = get_likely_move()
    beat_move = beat[expected_opp_move]
    
    output = beat_move
    
    # Otherwise make a random move (odds 1/3)
    if not output:
        output = random.choice(["R", "P", "S"])
    
    last_output = output