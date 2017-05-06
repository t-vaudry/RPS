## Name: c6
## Author: DegaLaman
## Used 'fifth-order losing markov chain' by 'rfw' as a reference
if not input:
    AeXtj = "RPS"
    CGFFI = gPuQG = NOeHx = sUqDN = ""
    CJgVl = [-1,-5,-29,-149]
    EUvcU = KkVLP = Reetc = QPImQ = XuhKb = eLafS = eagmk = 0
    EmCuy = [-1,-3,-11,-37,-113]
    LtWHg = lambda ODjZq: ODjZq[1]
    KDKSk = {AeXtj[0]:AeXtj[2],AeXtj[1]:AeXtj[0],AeXtj[2]:AeXtj[1]}
    PxDzO = [1,5,29,149]
    ZbZLg = [1,3,11,37,113]
    class KeObw(dict):
        def __missing__(mnAOo,XUAcF):
            zjQXt = {"R":XUAcF[0]=="R","P":XUAcF[0]=="P","S":XUAcF[0]=="S"}
	    mnAOo.__setitem__(XUAcF,zjQXt)
	    return zjQXt
    GNxJy = gbZTP = KeObw()
    fEyOc = "RS"
    from random import choice as jdheN
    jkoQG = {AeXtj[0]:fEyOc,AeXtj[1]:AeXtj[0:-1],AeXtj[2]:AeXtj[-2:]}
    nlefk = {AeXtj[0]:AeXtj[1],AeXtj[1]:AeXtj[2],AeXtj[2]:AeXtj[0]}
    output = jdheN(AeXtj)
    takSe = dict.iteritems
    wQyXm = sorted
    wcKNJ = {AeXtj[0]:AeXtj[0:-1],AeXtj[1]:AeXtj[-2:],AeXtj[2]:fEyOc}
elif not QPImQ:
    QPImQ = 1
    clDCG = input
    KPMHL = output
    output = jdheN(jkoQG[input])
else:
    GNxJy[clDCG[EmCuy[XuhKb]:]][input] += 1
    gbZTP[KPMHL[CJgVl[eLafS]:]][output] += 1
    clDCG = clDCG[EmCuy[-1]+1:]+input
    KPMHL = KPMHL[CJgVl[-1]+1:]+output
    if gPuQG != "":
        eagmk += gPuQG == nlefk[input]
        Reetc += input != nlefk[sUqDN]
        KkVLP += input != nlefk[NOeHx]
        EUvcU += CGFFI == nlefk[input]
    sQnrN = wQyXm(takSe(GNxJy[clDCG[EmCuy[XuhKb]:]]),key=LtWHg)
    if sQnrN[-1][1] == 0:
        nvQAl = AeXtj
    elif sQnrN[-1][1] == sQnrN[-2][1]:
        if sQnrN[-2][1] == sQnrN[-3][1]:
            nvQAl = AeXtj
        else:
            nvQAl = sQnrN[-1][0]+sQnrN[-2][0]
    else:
        nvQAl = sQnrN[-1][0]
    WEgFA = wQyXm(takSe(gbZTP[KPMHL[CJgVl[eLafS]:]]),key=LtWHg)
    if WEgFA[-1][1] == 0:
        vAwWS = AeXtj
    elif WEgFA[-1][1] == WEgFA[-2][1]:
        if WEgFA[-2][1] == WEgFA[-3][1]:
            vAwWS = AeXtj
        else:
            vAwWS = WEgFA[-1][0]+WEgFA[-2][0]
    else:
        vAwWS = WEgFA[-1][0]
    UWDGZ = jdheN(nvQAl)
    efEdj = jdheN(vAwWS)
    gPuQG = nlefk[UWDGZ]
    sUqDN = jdheN(jkoQG[UWDGZ])
    NOeHx = jdheN(wcKNJ[efEdj])
    CGFFI = KDKSk[efEdj]
    if eagmk < Reetc:
        xHPaP = (sUqDN,Reetc)
    else:
        xHPaP = (gPuQG,eagmk)
    if EUvcU < KkVLP:
        nylrp = (NOeHx,KkVLP)
    else:
        nylrp = (CGFFI,EUvcU)
    output = xHPaP[0]
    if xHPaP[1] < nylrp[1]:
        output = nylrp[0]
    QPImQ += 1
    if XuhKb != 4:
        XuhKb += ZbZLg[XuhKb+1] == QPImQ
    if eLafS != 3:
        eLafS += PxDzO[eLafS+1] == QPImQ