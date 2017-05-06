import random

history = []
beats = {"R":"P", "P":"S", "S":"R"}
call_sign = {"R":-1, "P":0, "S":1}
inverse_call_sign = {-1:"R", 0:"P", 1:"S"}
if input =="":
    output = random.choice(["R", "P", "S"])
elif len(history)<5:
    output = random.choice(["R", "P", "S"])
    history.append(beats[input])
else:
    #Sums up list
    sum = sum([call_sign[x] for x in history])
    output = inverse_call_sign[s_round(sum)]
def s_round(num):
    if abs(num-0)<0.5:
        return 0
    if num>0:
        return 1
    else:
        return -1