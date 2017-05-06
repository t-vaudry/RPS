# Name : The Great Loser
# Author : DegaLaman
# To Lose Is Not Difficult
# Version 0.0
if input=="":
    loses_to = {"R":"P","P":"S","S":"R"}
    wins_against = {"R":"S","S":"P","P":"R"}
    strategy_cnt = [1,1,1,0,0]
    strategy_func = {"R" : lambda: "R",\
                     "P" : lambda: "P",\
                     "S" : lambda: "S",\
                     "!" : lambda: loses_to[input],\
                     "!!" : lambda: wins_against[input]}
    strats = ["R","P","S","!","!!"]
    mine = "R"
    cur_strategy = "R"
    last = ""
    history = ""
    count = 0
    fixed = ""
elif fixed != "":
    mine = strategy_func[fixed]()
else:
    if count < 50:
        count += 1
        history += input
        if count == 50:
            up_against_fixed = True
            for each in history:
                if last != each:
                    up_against_fixed = False
                    break
            if up_against_fixed:
                fixed = wins_against[last]
    i_won = input == wins_against[mine]
    # Basic Strategies
    strategy_cnt[0] += (input != wins_against["R"]) - 0.5*(input == "R")
    strategy_cnt[1] += (input != wins_against["P"]) - 0.5*(input == "P")
    strategy_cnt[2] += (input != wins_against["S"]) - 0.5*(input == "S")
    # Less Basic Strategies
    if last == "":
        last = input
    else:
        strategy_cnt[3] += input != wins_against[loses_to[last]]
        strategy_cnt[4] += input != wins_against[wins_against[last]]
    if i_won:
        big = max(strategy_cnt)
        for i,each in enumerate(strats):
            if strategy_cnt[i] == big:
                cur_strategy = each
                break
    mine = strategy_func[cur_strategy]()
output = mine