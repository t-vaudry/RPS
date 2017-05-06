import random


if input == "":
    i = 0
    my_recent_win_count = 0
    opp_win_count_diff = 0
    opp_wins = 0
    opp_recent_win_count = 0
    my_wins = 0
    old_my_throws = []
    old_opp_throws = []

if input != "":
    old_opp_throws.append(input)
    old_my_throws.append(output)

    if((old_opp_throws[i-1] == "P" and old_my_throws[i-1] =="R") or (old_opp_throws[i-1] == "R" and old_my_throws[i-1] =="S") or (old_opp_throws[i-1] == "S" and old_my_throws[i-1] =="P")):
        opp_wins = opp_wins + 1
        opp_recent_win_count = opp_recent_win_count + 1
    elif((old_opp_throws[i-1] == "P" and old_my_throws[i-1] =="S") or (old_opp_throws[i-1] == "R" and old_my_throws[i-1] =="P") or (old_opp_throws[i-1] == "S" and old_my_throws[i-1] =="R")):
        my_wins = my_wins + 1
        my_recent_win_count = my_recent_win_count + 1
    else:
        pass
    
    last_opp_throw = input
    last_my_throw = output

    opp_win_count_diff = opp_wins - my_wins

if my_recent_win_count >= 1:
    opp_recent_win_count = 0

#--------Starting Throws--------
#Throw S or P to start ->
#                          Paper is most commonly thrown by females to start play
#                          Rock is most commonly thrown by males to start play
#Counter to Paper is S
#Counter to Rock is P
last_option = 0

if input == "" or len(old_my_throws) < 4:
    output = random.choice(["S","P"])
    last_option = 1

#If we lost a bunch in a row throw randomly
if opp_recent_win_count >= 10:
        output = random.choice(["R","P","S"])
        last_option = 87

#If we lost 2 or more in a row check for a 3 in a row pattern
#Override the random throw if there is a possible 3 in a row incoming. EX:RRR, SSS, PPP
if opp_recent_win_count >= 2:
    if old_opp_throws[len(old_opp_throws) -1] == old_opp_throws[len(old_opp_throws) -2]:
        two_throw = old_opp_throws[len(old_opp_throws) -1]
        if two_throw == "R":
            output = "P"
        if two_throw == "S":
            output = "R"
        if two_throw == "P":
            output = "S"
        last_option = 2


#If the opponents win total is 4 more than ours and we have not chosen an option
#throw R because people who are ahead tend to throw S
if opp_win_count_diff >= 4 and last_option == 0:
    output = "R"
    last_option = 3

#If we are winning by 4 and have not chosen an option throw P because
#people behind tend to throw R
if opp_win_count_diff <= -4 and last_option == 0:
    output = "P"
    last_option = 4

#If they one the last round and nothing above has been chosen counter their last move
if opp_recent_win_count >= 1 and last_option == 0:
    if last_opp_throw == "R":
        output = "P"
    if last_opp_throw == "S":
        output = "R"
    if last_opp_throw == "P":
        output = "S"
    last_option = 5

i = i + 1