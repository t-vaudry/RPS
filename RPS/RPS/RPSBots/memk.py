import random, math

K = 3
CAP = 3 ** (2 * K) + 3

def win (a, b):
    return (a + 1) % 3 == b

def prob_choose (cur):
    tchoice = cur[0] + cur[1] + cur[2]
    seed = random.randint (0, tchoice - 1)
    if (seed < cur[0]):
	return 0
    elif (seed < cur[0] + cur[1]):
	return 1
    else:
	return 2

def best_choose (cur):
    if (cur[0] > cur [1] and cur[0] > cur[2]):
	return 0
    elif (cur[1] > cur[2]):
	return 1
    else:
	return 2

#make array of moves for given state and randomly sample from those moves
def move (a):
    global output
    output = state [a]
    mymove.append (a)

def get_key (a):
    key = 0
    for i in range (a, a + K):
	key = 9 * key + 3 * mymove [i] + oppmove [i]
    return key

if input == "":
    state = ["R","S","P"]
    counter = ["P", "R", "S"] 
    st = [0,1,2]
    cntr = [2,0,1]
    sdic = {"R":0, "S":1, "P":2}

    freq = [[1 for j in range (3)] for i in range (CAP)]

    mymove = []
    oppmove = []
else:
    oppmove.append (sdic[input])
    #assert len (oppmove) == len (mymove) and len (oppmove) == N


N = len (oppmove)

if (N > K):
    freq [get_key (N - K - 1)][sdic[input]] += 1
    cur = freq [get_key (N - K)]
    
    mv = cntr [prob_choose (cur)]
    move (mv)
else:
    move (random.randint (0,2))