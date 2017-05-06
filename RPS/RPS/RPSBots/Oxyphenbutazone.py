# see also www.dllu.net/rps/

import random
if not input:
    numpre = 24
    nummeta = 6
    numlimits = 4
    limits = [3,5,7,8]
    vocab = [[],[],[],[]]
    vocab2 = [[],[],[],[]]
    for i in range(numlimits):
        limit = limits[i]
        timil = 3**limit
        vocab[i]  = [0]*timil
        vocab2[i] = [0]*timil
    t = 0
    q = [0]*8
    p = [0]*8
    rps_123 = {'R':0, 'P':1, 'S':2}
    output = ""
    out_ = random.choice([0,1,2])
    pScore=[[5]*numpre,[5]*numpre,[5]*numpre,[5]*numpre,[5]*numpre,[5]*numpre]
    mScore=[5,2,5,2,4,2]
    meta=[out_]*nummeta
    pred = [out_]*numpre
    dithering = 0.7
else:
    in_ = rps_123[input]
    for i in range(numlimits):
        limit = limits[i]
        timil = 3**limit
        q[i] = (q[i]*3 + in_) % timil
        p[i] = (p[i]*3 + out_) % timil
    for i in range(numpre):
        pp = pred[i]
        bpp = (pp+1)%3
        bbpp = (bpp+1)%3
        pScore[0][i]=0.9*pScore[0][i]+((in_==pp)-(in_==bbpp))*3
        pScore[1][i]=0.9*pScore[1][i]+((out_==pp)-(out_==bbpp))*3
        pScore[2][i]=0.9*pScore[2][i]+(in_==pp)*3.3-(in_==bpp)*1.2-(in_==bbpp)*2.3
        pScore[3][i]=0.9*pScore[3][i]+(out_==pp)*3.3-(out_==bpp)*1.2-(out_==bbpp)*2.3
        pScore[4][i]=(pScore[4][i]+(in_==pp)*3)*(1-(in_==bbpp))
        pScore[5][i]=(pScore[5][i]+(out_==pp)*3)*(1-(out_==bbpp))
    for i in range(nummeta):
        mScore[i]=0.96*(mScore[i]+(in_==meta[i])-(in_==(meta[i]+2)%3)) + (random.random()-0.5)*dithering
    if t >= max(limits):
        for j in range(numlimits):
            limit = limits[j]
            timil = 3**limit
            vocab[j][q[j]] += 1
            vocab2[j][p[j]] += 1
            maxq = [0,0,0]
            maxp = [0,0,0]
            for i in range(3):
                maxq[i] = vocab[j][(q[j]*3+i) % timil] + random.random()*0.5
                maxp[i] = vocab2[j][(p[j]*3+i) % timil] + random.random()*0.5
            pred[0+2*j] = maxq.index(max(maxq))
            pred[1+2*j] = (maxp.index(max(maxp))+1)%3
        for i in range(numpre/3, numpre):
            pred[i] = (pred[i-numpre/3] + 1)%3

        for i in range(0, nummeta):
            meta[i] = pred[pScore[i].index(max(pScore[i]))]
        for i in range(1, nummeta, 2):
            meta[i] = (meta[i]+1)%3

        out_ = (meta[mScore.index(max(mScore))]+1)%3
    else:
        out_ = random.choice([0,1,2])
output = "RPS"[out_]
t += 1