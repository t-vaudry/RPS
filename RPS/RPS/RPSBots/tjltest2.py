import random

ROCK = 'R'
PAPER = 'P'
SCISSORS = 'S'

try:
   assert initialised == True
except:

   initialised = True
   n_gram_length = 4
   tot_rocks = 1
   tot_papers = 1
   tot_scissors = 1

   move_history = []
   their_move_history = []
   last_output = None


def rand_move():
   rnum = random.random()
   if rnum < (1 / tot_rocks):
       return ROCK
   elif rnum < (1 / tot_papers):
       return PAPER
   else:
       return SCISSORS

if not input:
    move_list = []
    output = rand_move()
    last_output = output

else:

    last_pair = (input, last_output)
    move_history.append(last_pair)
    their_move_history.append(input)

    if input == ROCK:
        tot_rocks += 1
    elif input == PAPER:
        tot_papers += 1
    else:
        tot_scissors += 1


    last_n = move_history[-1*n_gram_length:]

    output = rand_move()
    last_output = output