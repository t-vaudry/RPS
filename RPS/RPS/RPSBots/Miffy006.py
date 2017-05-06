import random

if not input:
    history =   []
    output  =   random.choice(['R','P','S'])
    last    =   ''
elif len(history)==0:
    output  =   random.choice(['R','P','S'])
else:
    history[-1].append(input)
    data    =   filter(lambda z:z[0]==last,history[-50:])
    lData   =   float(len(data))
    if lData:
        pRock   =   len(filter(lambda z:z[1]=='R',data))/lData+random.random()*0.2
        pPaper  =   len(filter(lambda z:z[1]=='P',data))/lData+random.random()*0.2
        pSciss  =   len(filter(lambda z:z[1]=='S',data))/lData+random.random()*0.2

        if max([pRock,pPaper,pSciss]) < 0.5:
            output  =   random.choice(['R','P','S'])
        elif pRock > pPaper and pRock > pSciss:
            output  =   random.choice(['R','P'])
        elif pPaper > pRock and pPaper > pSciss:
            output  =   random.choice(['P','S'])
        else:
            output  =   random.choice(['R','S'])
    else:
        output = random.choice(['R','P','S'])
if last:
    history.append([last])
last    =   output