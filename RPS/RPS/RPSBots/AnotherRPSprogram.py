import random

# Did they win?
def win (yours, theirs):
    if (yours == theirs):
        return 0.5
    elif (theirs == "R"):
        if (yours == "P"):
            return 1
        else:
            return 0
    elif (theirs == "P"):
        if (yours == "R"):
            return 0
        else:
            return 1
    elif (theirs == "S"):
        if (yours == "R"):
            return 1
        else:
            return 0
    
play = ""

wins = 0
losses = 0
draws = 0

last_play = ""
last_response = ""
last_result = 0

input = ""

it = 0

responses = ["R", "P", "S"]

rand = 0.20 + ((float(wins) / (float(it) + 1.0)) / 10.0)

play = input 

if (it == 0):
    output = "P"
else:
    if (last_result == 0):
        output = responses[responses.index(last_response) - 1]
    elif (last_result == 1):
        output = responses[responses.index(last_response) + 1 if last_response != "s" else 0]            
    if (rand > random.random() or last_result == 0.5):
        output = random.choice(responses)
    if (win (output, play) == 1):
        last_result = 1
    elif (win (output, play) == 0.5):
        last_result = 0.5
    elif (win (output, play) == 0):
        last_result = 0

    last_response = output
    it += 1