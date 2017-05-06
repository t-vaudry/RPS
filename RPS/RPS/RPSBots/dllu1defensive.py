# see also www.dllu.net/rps
# This is another mostly rfind-based bot.
# Compared with dllu1, dllu1_defensive implements some defensive measures. The defense mechanism here isn't quite as agressive as, say, the derp_v6 program by evolvingstuff (which gets more and more random the more it loses, until it finally switches to nihilism whereupon it becomes totally random) that scores 48% against zai_all_switch_meta_corrector. But too much defending also reduces overall effectiveness against weaker bots.
# Due to the increased amount of randomness, dllu1_defensive has a slightly lower overall win rate (by about 0.2%) against an arbitrary pool of 39 bots. But it is slightly less bad against zai_all_switch_meta_corrector and fares well against the original dllu1.

# The key differences are:
# 1) dithering. Some random noise is added to the metapredictor scores.
# 2) more randomness when maximum metapredictor score is below a threshold (which indicates that none of the metapredictors are very effective).

'''
	dllu1, dllu1_defensive versus bayes14:
	
	bots/dllu1.py: won 79.2% of matches (396 of 500)
    won 35.3% of rounds (176595 of 500000)
    avg score 23.2, net score 11624.0, time 116037.42636
	
	bots/dllu1_defensive.py: won 79.0% of matches (395 of 500)
    won 34.9% of rounds (174737 of 500000)
    avg score 19.6, net score 9797.0, time 117635.02678
	
	bots/bayes14.py: won 20.1% of matches (201 of 1000)
    won 33.0% of rounds (329911 of 1000000)
    avg score -21.4, net score -21421.0, time 266629.78977
	
	--------------------------------------------------
	dllu1, dllu1_defensive versus zai_all_switch_meta_corrector:
	
	bots/zai_all_meta_switch_corrector.py: won 80.3% of matches (803 of 1000)
    won 34.9% of rounds (348731 of 1000000)
    avg score 26.8, net score 26836.0, time 95782.26727
	
	bots/dllu1_defensive.py: won 33.2% of matches (166 of 500)
    won 32.9% of rounds (164574 of 500000)
    avg score -9.9, net score -4943.0, time 116385.98595
	
	bots/dllu1.py: won 4.6% of matches (23 of 500)
    won 31.5% of rounds (157321 of 500000)
    avg score -43.8, net score -21893.0, time 114404.34772
	
	--------------------------------------------------
	dllu1 versus dllu1_defensive:
	
	bots/dllu1_defensive.py: won 76.0% of matches (380 of 500)
    won 34.6% of rounds (172993 of 500000)
    avg score 17.9, net score 8960.0, time 115415.65399
	
	bots/dllu1.py: won 23.2% of matches (116 of 500)
    won 32.8% of rounds (164033 of 500000)
    avg score -17.9, net score -8960.0, time 113650.73649
'''

# for more results for dllu1 and dllu1_defensive against an arbitrary pool of strong bots, see: http://pastebin.com/59kCHq3r

import random
numPre = 30
numMeta = 6
if not input:
    limit = 8
    beat={'R':'P','P':'S','S':'R'}
    moves=['','','','']
    pScore=[[5]*numPre,[5]*numPre,[5]*numPre,[5]*numPre,[5]*numPre,[5]*numPre]
    centrifuge={'RP':0,'PS':1,'SR':2,'PR':3,'SP':4,'RS':5,'RR':6,'PP':7,'SS':8}
    centripete={'R':0,'P':1,'S':2}
    soma = [0,0,0,0,0,0,0,0,0];
    rps = [1,1,1];
    a="RPS"
    best = [0,0,0];
    length=0
    p=[random.choice("RPS")]*numPre
    m=[random.choice("RPS")]*numMeta
    mScore=[5,2,5,2,4,2]
    dithering = 0.7
else:
    for i in range(numPre):
        pp = p[i]
        bpp = beat[pp]
        bbpp = beat[bpp]
        pScore[0][i]=0.9*pScore[0][i]+((input==pp)-(input==bbpp))*3
        pScore[1][i]=0.9*pScore[1][i]+((output==pp)-(output==bbpp))*3
        pScore[2][i]=0.87*pScore[2][i]+(input==pp)*3.3-(input==bpp)*1.2-(input==bbpp)*2.3
        pScore[3][i]=0.87*pScore[3][i]+(output==pp)*3.3-(output==bpp)*1.2-(output==bbpp)*2.3
        pScore[4][i]=(pScore[4][i]+(input==pp)*3)*(1-(input==bbpp))
        pScore[5][i]=(pScore[5][i]+(output==pp)*3)*(1-(output==bbpp))
    for i in range(numMeta):
        mScore[i]=0.96*(mScore[i]+(input==m[i])-(input==beat[beat[m[i]]])) + (random.random()-0.5)*dithering
    soma[centrifuge[input+output]] +=1;
    rps[centripete[input]] +=1;
    moves[0]+=str(centrifuge[input+output])
    moves[1]+=input
    moves[2]+=output
    length+=1
    for y in range(3):
        j=min([length,limit])
        while j>=1 and not moves[y][length-j:length] in moves[y][0:length-1]:
            j-=1
        i = moves[y].rfind(moves[y][length-j:length],0,length-1)
        p[0+2*y] = moves[1][j+i] 
        p[1+2*y] = beat[moves[2][j+i]]
    j=min([length,limit])
    while j>=2 and not moves[0][length-j:length-1] in moves[0][0:length-2]:
        j-=1
    i = moves[0].rfind(moves[0][length-j:length-1],0,length-2)
    if j+i>=length:
        p[6] = p[7] = random.choice("RPS")
    else:
        p[6] = moves[1][j+i] 
        p[7] = beat[moves[2][j+i]]
        
    best[0] = soma[centrifuge[output+'R']]*rps[0]/rps[centripete[output]]
    best[1] = soma[centrifuge[output+'P']]*rps[1]/rps[centripete[output]]
    best[2] = soma[centrifuge[output+'S']]*rps[2]/rps[centripete[output]]
    p[8] = p[9] = a[best.index(max(best))]
    
    for i in range(10,numPre):
        p[i]=beat[beat[p[i-10]]]
        
    for i in range(0,numMeta,2):
        m[i]=       p[pScore[i  ].index(max(pScore[i  ]))]
        m[i+1]=beat[p[pScore[i+1].index(max(pScore[i+1]))]]
output = beat[m[mScore.index(max(mScore))]]
if max(mScore)<3+random.random() or random.randint(3,40)>length:
    output=beat[random.choice("RPS")]