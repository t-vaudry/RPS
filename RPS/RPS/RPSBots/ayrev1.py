def get_transition_counts(history):
    r_cnt = p_cnt = s_cnt = 0
    last_pair = history[-1]
    for i in range(len(history) - 1):
        if history[i] == last_pair:
            next_opp_move = history[i + 1][0]
            if next_opp_move == 'R':
                r_cnt += 1
            if next_opp_move == 'P':
                p_cnt += 1
            if next_opp_move == 'S':
                s_cnt += 1
    return (r_cnt, p_cnt, s_cnt)

def win(x):
    if x == 'R':
        return 'P'
    if x == 'P':
        return 'S'
    if x == 'S':
        return 'R'    
        
def get_most_probable_move(r_prob, p_prob, s_prob):
    m = max(r_prob, p_prob, s_prob)
    if r_prob == m:
        return 'R'
    if p_prob == m:
        return 'P'
    if s_prob == m:
        return 'S'

def figure_our_move(expected_opp_move):
    return win(expected_opp_move)

if input == '':
    history = []
    output = 'R'
else:
    history.append((input, output))
    (r_prob, p_prob, s_prob) = get_transition_counts(history)
    expected_opp_move = get_most_probable_move(r_prob, p_prob, s_prob)
    output = figure_our_move(expected_opp_move)