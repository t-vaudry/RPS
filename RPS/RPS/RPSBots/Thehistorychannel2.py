import random
import re

history = 3

if input == "":
    num_moves = 0
    we_have_won = 0
    we_have_lost = 0
    his_context = ""
    my_context = ""
else:
    his_context += input

if num_moves < 100:
    output = random.choice(["R","P","S"])
else:
    # After being random for 100 moves I'm ready to try to predict how the opponent reacted to my moves or his moves
    # First we will scan the opponent context to see if we can find a previous occurrence of the last 3 moves
    his_last_moves = his_context[-history:]
    my_last_moves = my_context[-history:]
    his_actions = re.finditer(his_last_moves, his_context)
    his_stats = dict()
    his_stats["R"]=1
    his_stats["P"]=1
    his_stats["S"]=1
    for m in his_actions:
        if m.start()+history < len(his_context):
            his_move =  his_context[m.start()+history]
            his_stats[his_move]+=1
    # now scan my own context
    my_actions = re.finditer(my_last_moves, my_context)
    my_stats = dict()
    my_stats["R"]=0
    my_stats["P"]=0
    my_stats["S"]=0
    for m in my_actions:
        if m.start()+history < len(my_context):
            my_move =  my_context[m.start()+history]
            my_stats[my_move]+=1
    # Now for my stats we guess that he will counter so:
    his_stats["R"] = his_stats["R"] + my_stats["S"]
    his_stats["P"] = his_stats["P"] + my_stats["R"]
    his_stats["S"] = his_stats["S"] + my_stats["P"]
    
    the_options = ["R"]*his_stats["S"] + ["P"]*his_stats["R"] + ["S"]*his_stats["P"]
    output = random.choice(the_options)

my_context += output 


num_moves+=1