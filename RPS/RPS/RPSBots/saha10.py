import random

input=""
enemy = {'R':'P','P':'S','S':'R'}
dict = {'R':1 , 'P':1 , 'S':1}

win =0
loss = 0
continuos = 0

def weighted_choice():
    sum = 0
    #print dict['R'],dict['P'],dict['S']
    sum += (dict['R'] + dict['P'] + dict['S'])
    ran = random.randrange(0,sum)
    for key in dict.keys():
        if(dict[key]>ran):
            return enemy[key]
        ran -= dict[key]

def increase_weight():
    dict[input]+=1




if input=="":
    output =  "R"
else:
    output =  weighted_choice()
    if(enemy[input]==output):
            win+=1
            continuos = 0
    elif enemy[output]==input:
        loss+=1
        continuos+=1
    #reset
    if(continuos>=5):
        dict = {'R':1 , 'P':1 , 'S':1}

    increase_weight()