# beats beat last, beatbeatlast

# --------------------- initialization -----------------------------
if not input:
    import random, math
    import itertools, operator, collections
    
    R, P, S = 0, 1, 2
    RPS = [R, P, S]
    T, W, L = R, P, S
    PAYOFFS = [T, W, L]
    scorep = [0, 1, -1]
    to_win = [W, T, L]
    convert = {'R':R, 'P':P, 'S':S, R:'R', P:'P', S:'S'}
    subh = [[T, L, W], [W, T, L], [L, W, T]]
    addh = [[R, P, S], [P, S, R], [S, R, P]]
    ties, beats, loses = addh[T], addh[W], addh[L]
    POWER3 = [3 ** n for n in xrange(10)]
    
    op_hands = []
    my_hands = []
    payoffs = []
    op_payoffs = []
    
    output = convert[random.choice(RPS)]
# --------------------- turn -----------------------------
else:
    last_input, last_output = convert[input], convert[output]
    my_hands.append(last_output)
    op_hands.append(last_input)
    payoffs.append(subh[last_output][last_input])
    op_payoffs.append(subh[last_input][last_output])
    hands_played = len(op_hands)
    
    # bot initialization after first turn
    if hands_played == 1:
        mode = 0 # beat last
    elif mode == 0 and payoffs[-1] == T:
        mode = 1 # beatbeatlast
    elif mode == 0 and payoffs[-1] == L:
        mode = 2 # beat beatbeat last
    elif mode == 1 and payoffs[-1] == L:
        mode = 0 # back to beat last
    elif mode == 2 and payoffs[-1] == L:
        mode = 1 # beatbeatlast
    
    if mode == 0: # beat last
        next_hand = beats[last_input]
    elif mode == 1: # beat beat last
        next_hand = loses[last_output]
    elif mode == 2: # beat beat beat last
        next_hand = ties[last_output]
    
    output = convert[next_hand]