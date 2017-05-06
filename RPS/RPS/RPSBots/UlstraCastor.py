import random

if input == "":
    codify={
        'SS':'1',
        'RR':'2',
        'PP':'3',
        'SR':'4',
        'SP':'5',
        'RP':'6',
        'RS':'7',
        'PR':'8',
        'PS':'9',  
            }
    decodify={
        '1':'SS',
        '2':'RR',
        '3':'PP',
        '4':'SR',
        '5':'SP',
        '6':'RP',
        '7':'RS',
        '8':'PR',
        '9':'PS',
          }
    
    win={'P':'S','S':'R','R':'P'}
    score={'SS':0,'RR':0,'PP':0,
            'SR':1,'RP':1,'PS':1,
            'RS':-1,'SP':-1,'PR':-1,}
    history= ""
    enemy=[]
    mymove=''
    enemymove=''
    output=random.choice(["R","P","S"])
    strategy=[output]*19
    switching=[0]*19
    metastrategy0= ""
    metastrategy1= ""
    sscore=[0]*3
    optimal=2
    opt=7
    prediction=''

else:
    history += codify[input+output]
    enemy.append(input)
    enemymove +=input
    mymove+= output
    sc=score[input+output]


    for i,p in enumerate(strategy):
        s=score[input+p]
        if s==-1:
            switching[i]=0
        else:
            switching[i] += s


    if sc==-1:
        m=max(switching)
        optimal=switching.index(m)
            
    strategy[6]=win[random.choice(enemy)]

    

    for length in range (min(10,len(history)-1),0,-1):
        find=history[-length:]
        pos=history.rfind(find,0,-1)
        if pos != -1:
            prediction=decodify[history[pos+length]]
            my=prediction[1]
            en=prediction[0]
            strategy[0]=win[en]
            strategy[1]=win[win[en]]
            strategy[2]=en
            strategy[3]=win[my]
            strategy[4]=win[win[my]]
            strategy[5]=my
            break
        
    for length in range (min(10,len(mymove)-1),0,-1):
        find=mymove[-length:]
        pos=mymove.rfind(find,0,-1)
        if pos != -1:
            my=mymove[pos+length]
            en=enemymove[pos+length]
            strategy[7]=win[en]
            strategy[8]=win[win[en]]
            strategy[9]=en
            strategy[10]=win[my]
            strategy[11]=win[win[my]]
            strategy[12]=my
            break

    for length in range (min(10,len(enemymove)-1),0,-1):
        find=enemymove[-length:]
        pos=enemymove.rfind(find,0,-1)
        if pos != -1:
            my=mymove[pos+length]
            en=enemymove[pos+length]
            strategy[13]=win[en]
            strategy[14]=win[win[en]]
            strategy[15]=en
            strategy[16]=win[my]
            strategy[17]=win[win[my]]
            strategy[18]=my
            break
        
   
    output=strategy[optimal]