#this is almost entirely copiet from "Cabu"'s "Markov (speedup)"
#but a bit optimised
import random

moves = ['R', 'P', 'S']
beat_move = {'R': 'P', 'P': 'S', 'S': 'R'}

output = ''

if input == '':
    opp_history = ''
    x = -1
else:
    opp_history += input

    for length in (119,91,70,54,41,31,24,19,14,11,9,8,7,6,5,4,3,2,1):
        # Search for the last longest chain
        x = opp_history[:-1].rfind (opp_history[-length:])
        if x >= 0:
            # If found: Pick what will be the next move and play against it
            next_move = opp_history[x + length]
            output = beat_move[next_move]
            break

if output == '':
    output = random.choice (moves)
#x=0:18;
#a = 1.7;%1.36
#y = a.^((x/2));
#y(1) = 1;
#for i = 2:length(x)
#    if round(y(i)) > round(y(i-1))
#        y(i) = round(y(i));
#    else
#        y(i) = y(i-1)+1;
#    end
#end
#y(end:-1:1)