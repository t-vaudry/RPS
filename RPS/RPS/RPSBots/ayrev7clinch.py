import math, random

def get_transition_counts(history):
    r_cnt = p_cnt = s_cnt = 0.0
    last_pair = history[-1]
    n = len(history) - 1
    i = n - 2
    boundary = max(n - depth, 0) 
    while i > boundary:
        if history[i] == last_pair:
            next_opp_move = history[i + 1][0]
            if next_opp_move == 'R':
                r_cnt += weight(i, n)
            if next_opp_move == 'P':
                p_cnt += weight(i, n)
            if next_opp_move == 'S':
                s_cnt += weight(i, n)
        i -= 1
    return (r_cnt, p_cnt, s_cnt)

def weight(i, n):
    return math.pow(0.236927758682, (i - n)*(i - n))
        
def get_most_probable_move(r_prob, p_prob, s_prob):
    m = max(r_prob, p_prob, s_prob)
    if r_prob == m:
        return 'R'
    if p_prob == m:
        return 'P'
    if s_prob == m:
        return 'S'

def figure_our_move(x):
    if x == 'R':
        return 'P'
    if x == 'P':
        return 'S'
    if x == 'S':
        return 'R'   

if input == '':
    history = []
    output = 'R'
    depth = 300
    balance = 0
    turn = 0
    score  = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1, 'RP': -1, 'SR': -1, 'PS': -1,}
    run_algo = True
else:
    history.append((input, output))
    balance += score[output + input]
    if turn == 40:
        if balance < 0:
            run_algo = False
    if run_algo == True:
        (r_prob, p_prob, s_prob) = get_transition_counts(history)
        expected_opp_move = get_most_probable_move(r_prob, p_prob, s_prob)
        output = figure_our_move(expected_opp_move)
    else:
        output = random.choice(["R","P","S"])
    turn += 1