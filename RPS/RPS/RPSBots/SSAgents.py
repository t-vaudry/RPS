import random

def calcWinLose():
    global win_count
    global lose_count
    global draw_count

    win_count = 0
    lose_count = 0
    draw_count = 0


    for round in choices.split(","):
        if round == "SP" or round == "RS" or round == "PR":
            win_count+=1
        elif round[:1] == round[-1:]:
            draw_count+=1
        else:
            lose_count+=1

    return

def get_max_val_key(hashmap):
     """Return key of max_val from hashmap"""
     values = list(hashmap.values())
     return hashmap.keys()[values.index(max(values))]

def find_pattern(haystack, needle):
    """Returns positions of needle substring in s"""
    #print "find "+needle+" in "+haystack
    haystack_temp = haystack
    pos = []
    offset = 0
    k = haystack_temp.find(needle)
    while k != -1:
        k = haystack_temp.find(needle)
        if k == -1:
            break
        pos.append(k+offset)
        #print " "+haystack_temp+' '+str(k)

        haystack_temp = haystack_temp[k+1:]
        offset = offset + k +1
    return pos

def find_pattern_tails(haystack, needle, tail_offset):
    """Returns hasmap of needle substring tails in s"""
    pos = find_pattern(haystack[:-(tail_offset+1)], needle)
    # [:-X], we need only patterns with tails
    tails = {}
    for i in pos:
        tail = haystack[i+len(needle)+tail_offset]
        #print str(i)+"="+tail
        if tail in tails:
            tails[tail] += 1
        else:
            tails[tail] = 1
    return tails
def get_highest_tail(haystack, needle, tail_offset):
    """ Returns highest tail val"""
    tails = find_pattern_tails(haystack,needle,tail_offset)
    if len(tails):
        #print normalize_hashmap(tails)
        return get_max_val_key(normalize_hashmap(tails))
    else:
        return None


def normalize_hashmap(hashmap):
    """normalize the hashmap """
    hash_sum = 0

    for key in hashmap.keys():
        hash_sum += hashmap[key]
    for key in hashmap.keys():
        hashmap[key] = hashmap[key] / float(hash_sum)

    return hashmap

def agent_pattern_length(pattern_length):
    """Predict the opponent move by seraching patterns in the match data, imput = length"""
    move={"R":0,"P":0,"S":0}
    pattern_len=3*pattern_length
    last_pattern=choices[-pattern_len:]
    tails_his=find_pattern_tails(choices,last_pattern,1)
    if not len(tails_his):
        return None
    else:
        expectation_his=normalize_hashmap(tails_his)
        for move_his in expectation_his.keys():
            move[BEAT[move_his]]=expectation_his[move_his]
        return move

def agent_pattern_3():
    """Predict the opponent move by seraching patterns in the match data"""
    return agent_pattern_length(3)

def agent_pattern_4():
    """Predict the opponent move by seraching patterns in the match data"""
    return agent_pattern_length(4)

def agent_pattern_5():
    """Predict the opponent move by seraching patterns in the match data"""
    return agent_pattern_length(5)

def agent_pattern_6():
    """Predict the opponent move by seraching patterns in the match data"""
    return agent_pattern_length(6)

def agent_random():
    """ Random move, good for testing """
    move={"R":random.random(),"P":random.random(),"S":random.random()}
    return move

def agent_repeater():
    """ Beats the opp last move """""
    move={"R":0,"P":0,"S":0}
    move[BEAT[input]] = 1
    return move

def agent_counter():
    """ Counts freq of the opp move """""
    global rockCount,paperCount,scissorsCount
    move={"R":0,"P":0,"S":0}

    if input == "R":
	rockCount += 1
    elif input == "P":
	paperCount += 1
    elif input == "S":
	scissorsCount += 1

    if rockCount > paperCount and rockCount > scissorsCount:
	good = "P"
    elif paperCount > scissorsCount:
	good = "S"
    else:
	good = "R"

    move[good] = 1
    return move


if input == "":
    rockCount = 0
    paperCount = 0
    scissorsCount = 0 #agent_counter

    BEAT = {'P': 'S', 'S': 'R', 'R': 'P'}
    BEAT_SCORE = {'RR': 0, 'PP': 0, 'SS': 0, 'PR': 1, 'RS': 1, 'SP': 1,'RP': -1, 'SR': -1, 'PS': -1}
    score={}
    moves_count={}
    move_last={}
    score_shift={0:{},1:{},2:{}}
    agents=[agent_pattern_6,agent_repeater,agent_counter,agent_random]
    for agent in agents:
        score[agent] = 0
        score_shift[0][agent] = 0
        score_shift[1][agent] = 0
        score_shift[2][agent] = 0

        moves_count[agent] = 0
#        move_last[agent]={}
    win_count = 0
    lose_count = 0
    draw_count = 0

    counter = 1
    choices = ""
    #output = random.choice(["R","P","S"])
    output = "S"
else:
    for agent in move_last.keys():
        score[agent] += BEAT_SCORE[move_last[agent]+input]
        score_shift[0][agent] += BEAT_SCORE[move_last[agent]+input]
        score_shift[1][agent] += BEAT_SCORE[BEAT[move_last[agent]]+input]
        score_shift[2][agent] += BEAT_SCORE[BEAT[BEAT[move_last[agent]]]+input]
        moves_count[agent] += 1


    calcWinLose()
    counter+=1
    choices+=input+','

#    output = "R"
    output = random.choice(["P","S","R"])
    move_last = {}
    agents_best=sorted(score,key=score.get,reverse=True)
    agents_best1=sorted(score_shift[1],key=score_shift[1].get,reverse=True)
    agents_best2=sorted(score_shift[2],key=score_shift[2].get,reverse=True)

    for agent in agents:
        move=agent()
        if move!=None:
            move_last[agent]=get_max_val_key(move) #Same values?{'P': 0, 'S': 0.5, 'R': 0.5}

    for agent_best in agents_best:
        if agent_best in move_last:
            output0 = move_last[agent_best]
            current_score0 = score_shift[0][agent_best]
            break

    for agent_best in agents_best1:
        if agent_best in move_last:
            output1 = BEAT[move_last[agent_best]]
            current_score1 = score_shift[1][agent_best]
            break

    for agent_best in agents_best2:
        if agent_best in move_last:
            output2 = BEAT[BEAT[move_last[agent_best]]]
            current_score2 = score_shift[2][agent_best]
            break

    output = output0
    if current_score0>current_score1 and current_score0>current_score2:
        output = output0
    if current_score1>current_score0 and current_score1>current_score2:
        output = output1
    if current_score2>current_score0 and current_score2>current_score1:
        output = output2


    if lose_count>win_count:
        output = random.choice(["P","S","R"])



choices+=output