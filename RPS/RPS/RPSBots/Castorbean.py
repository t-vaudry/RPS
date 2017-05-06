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
    codint={
          0:'0',
          1:'1',
          2:'2',
          3:'3',
          4:'4',
          5:'5',
          6:'6',
          7:'7',
          8:'8',
          9:'9',
           }
    decodint={
          '':1,
          '0':0,
          '1':1,
          '2':2,
          '3':3,
          '4':4,
          '5':5,
          '6':6,
          '7':7,
          '8':8,
          '9':9,
           }
    win={'P':'S','S':'R','R':'P'}
    score={'SS':0,'RR':0,'PP':0,
            'SR':1,'RP':1,'PS':1,
            'RS':-1,'SP':-1,'PR':-1,}
    history= ""
    enemy=[]
    output=random.choice(["R","P","S"])
    strategy=[output]*7
    switching=[0]*7
    metastrategy0= ""
    metastrategy1= ""
    sscore=[0]*3
    optimal=[0]*3
    opt=7
    prediction=''

else:
    history += codify[input+output]
    enemy.append(input)
    sc=score[input+output]

    for i in range(3):
        sscore[i] +=score[strategy[optimal[i]]+input]

    for i,p in enumerate(strategy):
        s=score[p+input]
        if s==-1:
            switching[i]=0
        else:
            switching[i] += s

        if s==1 and (i<3):
            metastrategy0 += codint[i]
        elif s==1 and (i<6):
            metastrategy1 += codint[i]

    if sc==-1:
        m=max(switching)
        optimal[0]=switching.index(m)
            
    strategy[6]=win[random.choice(enemy)]

    for length in range (min(10,len(metastrategy0)-1),0,-1):
        find=metastrategy0[-length:]
        pos=metastrategy0.rfind(find,0,-1)
        if pos !=1:
            optimal[1]=decodint[metastrategy0[pos+length]]

    for length in range (min(10,len(metastrategy1)-1),0,-1):
        find=metastrategy1[-length:]
        pos=metastrategy1.rfind(find,0,-1)
        if pos !=1:
            optimal[2]=decodint[metastrategy1[pos+length]]

    for length in range (min(10,len(history)-1),0,-1):
        find=history[-length:]
        pos=history.rfind(find,0,-1)
        if pos != -1:
            prediction=decodify[history[pos+length]]
            mymove=prediction[1]
            enemymove=prediction[0]
            strategy[0]=win[enemymove]
            strategy[1]=win[win[enemymove]]
            strategy[2]=win[win[win[enemymove]]]
            strategy[3]=win[mymove]
            strategy[4]=win[win[mymove]]
            strategy[5]=win[win[win[mymove]]]
            break

    m=max(sscore)
    opt=optimal[sscore.index(m)]
    output=strategy[opt]