import random

if input=="":
    model = { 'PP': {'P':0,'R':0,'S':0},
            'PR': {'P':0,'R':0,'S':0},
            'PS': {'P':0,'R':0,'S':0},
            'RP': {'P':0,'R':0,'S':0},
            'RR': {'P':0,'R':0,'S':0},
            'RS': {'P':0,'R':0,'S':0},
            'SP': {'P':0,'R':0,'S':0},
            'SR': {'P':0,'R':0,'S':0},
            'SS': {'P':0,'R':0,'S':0},}
    reply = { 'P':'SP','R':'RP','S':'SR'}
    output = random.choice(['R','P','S'])
    past = ""
else:
    temp = input+output
    if past =="": 
        past=temp
    else:
        model[past][input]+=1
        past=temp
    sum = model[temp]['P']+model[temp]['S']+model[temp]['R']
    if sum==0:
        output = random.choice(['R','P','S'])
    else:
        str = ('P'*model[temp]['P'])+('R'*model[temp]['R'])+('S'*model[temp]['S'])
        expect = random.choice(str)
        output = random.choice(reply[expect])
        past=temp