# Cargo Cult v0.1
import random
STRAT_RANDOM = True # include the random strategy
STRAT_DECAY = 0.97          # percent of score to retain over time
STRAT_DECAY_LOSING = 0.5    # decay rate when losing
STRAT_THRESH = 0    # strat must be this effective to be played
STRAT_NOISE = True  # include random noise even when a strategy is doing well
NOISE_CHANCE = .15  # use a strat this percent of the time if NOISE_RANDOM

# globals
STRATS = 25
if not STRAT_RANDOM:
    STRATS -= 1

def key_to_num(hist):
    d = {"P": "0", "R": "1", "S": "2"}
    num = "".join([d[i] for i in hist])
    return int(num, 3)

wld = {
    "R": "RPS",
    "P": "PSR",
    "S": "SRP",
}

scoring = {
    "R": {
        "R": 0,
        "P": -1,
        "S": 1
    },
    "P": {
        "R": 1,
        "P": 0,
        "S": -1
    },
    "S": {
        "R": -1,
        "P": 1,
        "S": 0
    }
}

if input == "":
    magic = """5&_$p&$o_$8_]mY$*($&$PpUJ);5&$opP5ll8pRGvU8ZL$Y7&pO8nh$&;_U4$1L$kl8pJ8IX5&_!pi)J15&5&9o$]28&;mp{b4G5P!&yC!}(5p%ip&&WX5gtdvb]q=8H$ov=&TC$[&&)D_C}PgHovHPtX$85oEG8@I5&55p($;R$8G&NL6&M_c8$HJ)7X$kU7VZ5&F&+hevt&TO)[)&-v!G1$31rnt$&;!)Y@@+n0J))}Fs^)E15&!$Bo$%S%pTny1$GD$42&lCJjX53$@pZMHz3jOpmtPy}xnGqy+$x[5o5Pk^!nAlsKMy#8UL&p2]*C!B15p{]cP&JG8pipm}nQ!)bb2Hz)4I$p;mmK%84*d[avzLyU9y{cmb&X1$Z}AU8)]i$ssmvtGC4&L+rvUDWI_9_8_8&Y#]Crop]NWh]&57e$*z1$CLmpKPY^LsL@mqppIpylZqZ8#C$tqGb]$O2lTkC*V*#R_=wCKFSF1$&$$Q&$&;$*_8p4S-]_[08kF!^F5&M&y&-BbY#$rm[osF$Xw-@^VS15]4op!=tX5!=^s2]R^5LL#!X8T15*LM}Z$!J&iG@m2rG!]=A[L();I&jb[awsj30jIxv4CtUfxP^yL5p=]=04ZqwI(f7eKy8FXL&bI^XX!F15$L5UU$S5VOPHj=)yY5x&0AAFXXVRC4jXGaw]qOlm1fjClO7{FpiX15CU+2FY614[R)mX[2X5TF;TIGF15&$$y&$a_$&k&y#9gX$r;iAS5-F552&{g!y(jmw3mY[g4&Llhsf6Pu$$;Yk$_2O&DLYy88C1]{#)3S)BI5&$&p*!s[$58-mqMhT_8GUt^$gC!B)jmhPQ9jv@dvg(gR!p;jvZLLL$K#OsbCx=]z4pp]yUC)U_fZJ&BR5&$)Ut5)n&85Sj=gwe5&!=jUlY}GQ8IKW5ccp6yNvUWok&ZHsg#p2L5%VL_U)]7^;O7mOPxC&pCeOXYU15p#&pU)2O@yjcm]MpU$Xn-A)r6C5twKm&Voejvpdmt8pkLUDpv&!AU5p][&&8SU@aj5vU#o^V9B2eu!a1$j7yma[jQ5arjmZ*d{;s7N{[0XFamkjmCS*=am#dvypzU8QI[vOQK18g_*m8$p8@dKZmQ&QUQ*C4yIfdI$pXNz=!Q6{Kv&d8Qy#&PTq^CPGUoj#wvLh@MspjamQapH@ypTyw=yI$q[H1C1tFjpF5vC&BL{]U^NUft1$&$&n&$YX5^M8y#$YR$8#Msa4iX5]8_yQqQ(pnLWmx-ypI1IeW*x1}$B&&8Y]XCoLl&p]DOU)UL8!cGz1$j^j*HjOR*9YayK8;8&ALXub@z1)HCpgoqb=kQF%vUyvkP(4XkL)XU$XGpy!FbeIm$yyQ#UU_X7FnLYE15mtPLC8*5*9tUdO&Q!Vx(Ct=gUU8tb^QUG;LGaX&ytgdUZFkL%FVR1$UXtk7&CC;TXU61EXU&HzCOU&RI5&$$*858]$8$8p&89=$)$]of!oX$&_&yG5AIxba_ye&X#&UP]jGgVI5P5&KU&sM]8gljCR43577OiX;j15r5&a]8Be$&8WyL$$S$$5$T=5-U$&7=jHQq}xa&dvyt}4QQHMsP_1R5(!r[5Y3PVKP+vrOFX]POCXXYN1$&)&k#8R}$8oPy4PSw8$5toULXX5p)=tnFiF4-FSvt(]X_Yrp3K]J15GVSF[_FI}Pt-jOMBI]=R[FO7z15p;oZf590$yExWU!A48kKDr[VN1_K^-vO)!SBjCymOPq#5Z2[j-GbC5g0&jt;]XEvN8mFaXO$8IUeFStI5TOKpS)jy8SXas1Ip(!SV^5GeF15jWKyXjs=rjKsvUepV{*Ujs-&yI]s&L[IMj1CKuevQCBXxFL(eLCFI$pO]Lu&FL&mkOptkpH]n@5[c&V1$$JxKWPUU)jKAdPbHL@1KzjNLEU8oao(U4XC)mtBsRkTR9=Ubs1C(1$&_$pM$&5&ypyWUSkP]C^OkD5iI$O]QLY&f!=utxmIqXe4U4C*8Ie15{!W=[;RF[UL2NX!^efR1Je=8XI&L4!K_AB3Y0HNWUxC[8UXO2C!i1$[U$s[tjL)O[omk](IUc#XTU)v18;{DoX[W}IwB^KX0XI&[41KL8115&cu=P5^IlUkIy]4kI8fo_W}LX1)#OTE(UiO)^XTmtPZI=[On#RHU1$H;LUCCO1CUCsaeUL1;bUU[R4C15&$5pr_*8$p9jm*^ZY_);8@g2J($p!opH))JomkBmLigt;U#]gx5tG5P!$PYJ;w)s)ij^}xR8I4YnHi715*#&x$8]Kr*)TvCVa=_&^vg)_bI)mBlg&!J=gv*ymKopC&y_jv58MU$kO&AD&DxxzsmmLOPU&yFGI*]J1$&]8pZ$P^]^L8d#fAq$_;)_S52X5sQos]!&UXmX)vn*9X^FslpgxBI$7(oZ*!WIOHOrmIP-C&sI)%hDI15j$&j*552)%!sma!oC$_7Xma5XO!pGmppyg*saopvtPZG0T!nyyc7C5gnTyI-U7&]k{mLzyy;2UoOU&HI8aW[dSr#kAmsmmUb{=i@=;aB{qt)jOsmt)QtjmCmmyyyUOyGsm3l1C5ptbg#zTL*jhQmkFnCdRknkR8KI$pKxS3!iHD6Lsm=@yP5U&MY79CU&yzpmypE7FwCsmU*sL&O9pjH^0F5p#-y#YkJO1OSmTXKz!x=Ne14O1$&;]t&5@]&%GbQCHwq!Mw#BCMUQ5&HEj2kg;&j&qpUt3qGXVFss8PI$*[xxeFbO)r)[T#3XO8^KLLF;z1$&O)nV&!YSjjwvw);z]y@1bR=]U^yXBvLpvhsmwWmn]F8NQkUynWnI&oKTs^^OCA-kOs#UXRLPa#nR011$$LCwS5f!8*LUZy&+C&&_#UHtkU]8CPs7{djnfXUmT1#L=&C#s1uU1$Q4S7]]OLOFFpv1hX18yUO0UGCI5@$]sL$)K!@SivY7iP!K^;s35d1!)2aabJP9mm3amT2yX-zgrmY86X5%)]3#LeYIkBipV5Xk]mT!dU4j1$lrj@&!aRAoYmmy$pO;#)XQDosI)@Blc8PpCsmyvmyypUqtLsv&xvC&[Mzs!pnGO@XydjXbU]p#^6}_H1${7&Ob;iB8c!XpC#gC$o9[l(G01!mk^-q;DI@smWmCbsEt[k7jzPXX&*VEHh)Tf1v]YjnWE1dtCw@IcBI$p#@jZ$OFjsK$mU*N})V!ra^raI;jWjmjkpOgswmvyavUopUZvp;IR$vTdsC^7XjsjXm^LsFYOOXKR8X1$d^jm[lGUKdJdmmPmL8jP#jKGj1idRmmvtpUsmZmmZ*mU$yamvqSN1Spt@j*[pUjpsjm#^W1^ybpvb=1I)p#VmxpBRaj8Pv#pQa&-H2yq4kIKjsWv*)sUqd(vmq&p#KyILvmin1$y#pyFoFUd^Cjm1yXR8TbTsRDnI5x_$gh$kt&pK;v4+Z18^t]*U8{1&p&mv6ug#WZWuvU*pC*Y4WyG&gU&*Dtt=UyU)mkey8FUCPURvtU;UI$B2sy9rZCrKt@mO*@REt*zWUG(ISj@jvrZjB@d(jmy*ZU@zCF1^tR1]T[*KUAULTmCsjOCIUHy4O1RGFI$pLCyUigk]=*=WUk&J]Q!V(R]hRP+XsyQG}4#sa[vX*pq&bY3m1C11$*%&Uh]=1m-bOTUF1RDU1kkRG115o58Kq8$P_j&9v^;G9$&A;T])g15]_&g]&zFmgO;vUf8}pUM%H65Fz5o!yvM&=U&7^Ps87yC;kUzcD&r1$k4&p*@sI88&*v=pkB&TuPptGORDm7ov8r+bfa{smppgL3y@-gC3gR]oUPV5xC1#itudSqTL$=1_FU&[1$*rPsb$PT&=QYp}UG=8r!8+(=tCl%Ntg_fY2=ksTmYUOIsHyZ-Yx(1$=FxL8Pj0=UOPjPUn18=C_T1C0I5j$)po5Xe)jA6vL;uX!LBxs}r_1MWSsdm^o^$jpjvU*;#pY^mZjC=I]vkkEBSnU9@kNvqDYRx2uLXLGK1$aCkmj;jn=3JjvHmg-3^y%aP&QR]j3nm]jaNPvfmmzqpt1U#jmRLOI&(Byvi(sbkUOZmmktI]CLLw1SO1$U=tg33nTj4=sNyR1t!o[6AV=CI#k&PmH4DU@jt@msk#U*U2{WmUC1&yLdLBK[CuJrosXIe1%HLkO1CR1$ZGE1b&-[&*9^pC8=c_L0$eX5Y1!*%Fbv9gFQgT-v7@@C1UL&tCpkU&*Imk=UUU&p=InF9]U4bUPj1CR15kELvYQF$T8^XmUKvk&8YXFC1BI5k(1sti3U)sKym}UsLk^CB1UxZ18GC&OFL7U-eLOvUIX1&#t4F17I1$QLkbU)SRxgLUyUoXU&yL#O1$I1&ZLfgU]HIUrv;s[ULRI#UnOR4zI5LR^{LU11oZRtO=FR1fU=!OLDI15&$5yY5&8$&$-Q&&ZC$M_oZ_&jU5%$)yG&LVo1U6v=oeU$]8&1G]##5&)$k!_pOlUL7p[DwX$)J]Kh!TI$o$8o8&rV]&]&mLGWf$&3}WA8-U)a%&ZG]f7vjuuvU(Q!*p3Us#DhI&U48o9&FU&x]ypx#)4&U[Z}F;RI5&_&yJ$&)]8&&ZUMt7$&);^UG[I5ptQgjJ5)#yKMmO][IULYYvUie1$4[{U_])1SUR;=tBXX_UX7aX5I15&_55(!g-$pj4pklZ]$G)*(DAc15y4NpEttZTpjavtxth]28nZ7MCC$&!1P1lUVuaWFpG#^CM!)K}C#zI8pM_gPTxO&jSvyQsyUpgm4w7&aO_@OpmnrjJjyXjmUUsUtyOXy@iUU&k&X15S@4@{ejpgp1bPj@XZCY11$&$_V8&Q*&ES5v=mtq8U4]-rQs18FS3+s{*]OWk_mRppCkLLyKq8yI5LI#U1PT12-C9sLgwC#bCC[O4I1$P$8H!5E2]Z]]p=L=L_&5Y*!V(1]y&Yyp=6-&bV&dCLLH&Y8PBn=I159&&V=1CX&&Ln+CZ1C]]LEjIIX15Q)$#Y)p_P&tnZ(GXF8AGU#FSt18910jXQT=!@X[vt4LUPDLXKUKiUPU#Y!VL1U4TLIT[LI1##L^nXCI159_&U=8HD5UG}B}Q1I_f4#bC1L1&[5py2P}n7[XJyXYO1)#UgsL411_Y&)7GXt1&_OKsX=1IoCU4[I4115&$8Q8$YR5p@PNO94O$yDA[]5Lz$f]8mL7]eMykovUOtY&Vk&*Q]91$3!kp3[e=4pLFyFT888UX5*O!sI$Sl]d#Mi!!&&jyy63^5O41ZObaI)j0umYxA!jjjjm1&db@Te7gL{WI5=@oA0!;=UUCapxOOUy9CpyhGFI$y;2yL]75P;=0jI*&I]&;bw4&O1!xjkWm85;;-kxmCoqUH8LOOa2c1$q9PUoY!VLOU1Bk)7IMt=OqOGF1$j=&tP6TO!ys;mU^Tr8[N!c$=NX;KXsmKysUlvKmmqksj7UQ)jRMtU$PUksC;UC@a@XjX2yOoNCV)RCQI$-TDpPsGY7jSjm*Qyn!f)RjpkX1ijOjmUVjXBmLvmzkyUgLCppUTHR-H&RpHkXXy*tmmLQkL){DHmL81I_{L]s}HmyP2l&{PLp7&Gb4141UIMZk#WTmjX$KA@mO^mLn;obWRLd1]QCCwhyi1POLX@1qmR&k##OI4z1$g_&ZD8BI]PLQW[#3#5Rt8=)6u1$kRodyktU(KU)yCUTCU1#jnYwFC]b]BWYULIyXQGKX1F18#UPXUbB1$NO(Tj=CL&+]jyq%JCPLzU1gFg1)tFTjJ^Agu%TjmX{tL#T[^^LL1U&LCkk0k[0KaU3KwF1UFUUFW1UL1$jMMP88]I]yI[KU_SU][nUO=UX18*c1G-9(R3TCrmFHKU&ZU4kL111!gUTibtCI5FUGOL4X18=Ikt1CI1$p_&QU_KV5(Vp{U]]}$}_ip^5I}_&]p6Q514$mL{vCcO0oUOzX1!215&5&hCMqC&[I&Ub#&CVLCcKO5XI5&V8s]&ED&G*&mt#=F&8JU(UpZ1op8k}P8}G$sXAv=PjFfqVbOCpQC8%GPm5880]kL=v=OL(f1U==UMF1$^V&Ti8_Y]])2yA;C4585WHC4LI8aFL35]80[;tAsXTURNUZnaIYX1&U[P[UGw5YUw#2w0wI5LR!KI=11$*$8ZU8;(olm@jZLbw8^Irr+Sd15ZLapA!8DYs5]vU&UP]U8SjH!cC5#qF#IVXOnTyUd}rnI8Uk1XF)41$-L2TRF1j)mk@dFpjX]MXXaIHO1$s^saNYeF)mevmLvnUxC=(s-Ls1]LtLk1JCI)knKv1UwUoLCXR1LqI&9C_DOoWRP9UAjCKTX&&__]GILR;=XAeLPuhnOXSmOnwUht(BTOJn18=C#TtCL1J7CIsOdXR8GtkO141I$m$&U=8h0]QpomL&CC]b_[HF5zC]LLtQ#CkUtLuAmLLtFUUF5sLgnI8LP#]4=L10nCJLFVO18UCnOICF1$&OxK#[7UO!SSjFc[O]UL^N1GF1_WO^mzSFRXaO-vRCwU)aVnvXgt1fUUrrUUX1SKFPn1UXIoB4F(RCR1&&1oUU&RC&UC)K1PCC5kG]eh1II_#=COX41U[O}aaX#E1GkUDwIIO1$yUo[CVOI84CJnFC1I8bI4R1C11"""
    chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]{};':",./<>?`~|\\"""
    x = "PRS"
    keys = ["".join([d, c, b, a]) for a in x for b in x for c in x for d in x]
    chant = dict(zip(map(lambda x: chars[x], xrange(len(keys))), keys))

    magic1 = []
    magic2 = []
    magic3 = []
    magic4 = []

    for i,c in enumerate(map(lambda x: chant[x], magic)):
        magic1.append(c[0])
        magic2.append(c[1])
        magic3.append(c[2])
        magic4.append(c[3])

    magic1 = "".join(magic1)
    magic2 = "".join(magic2)
    magic3 = "".join(magic3)
    magic4 = "".join(magic4)

    game = 0
    total_score = 0
    myhist = []
    youhist = []
    guesses = None

    score = dict.fromkeys(xrange(STRATS), 0) #XXX should be a list
    choicehist = [0] * STRATS # number of times the strat was the best choice
    playhist =  [0] * STRATS  # number of times the strat was actually played
else:
    game += 1
    youhist.append(input)

    # calculate current score
    total_score += scoring[output][input]

if len(youhist) < 8:
    output = random.choice("RPS")
    if STRAT_RANDOM:
        # XXX we may not want to actually track these
        # before the strat engine really starts...
        choicehist[0] += 1
        playhist[0] += 1
else:
    if guesses is None:
        guesses = []
    else:
        # evaluate strength of last guess
        for i in xrange(STRATS):
            if total_score > 0:
                score[i] *= STRAT_DECAY
            else:
                score[i] *= STRAT_DECAY_LOSING
            score[i] += scoring[guesses[i]][input]
        guesses = []

    if STRAT_RANDOM:
        guesses = [random.choice("RPS")]
    guesses.extend(wld[ magic1[key_to_num(myhist)] ])
    guesses.extend(wld[ magic1[key_to_num(youhist)] ])
    guesses.extend(wld[ magic2[key_to_num(myhist)] ])
    guesses.extend(wld[ magic2[key_to_num(youhist)] ])
    guesses.extend(wld[ magic3[key_to_num(myhist)] ])
    guesses.extend(wld[ magic3[key_to_num(youhist)] ])
    guesses.extend(wld[ magic4[key_to_num(myhist)] ])
    guesses.extend(wld[ magic4[key_to_num(youhist)] ])

    # find best strategies so far
    best = max(score.values())
    if best > STRAT_THRESH:
        choices = filter(lambda x: score[x] == best, xrange(STRATS))
        for choice in choices:
            choicehist[choice] += 1
    else:
        choices = [0]

    # do we add noise to the result?
    if STRAT_NOISE and random.random() < NOISE_CHANCE:
        if STRAT_RANDOM:
            # if we have the random strat enabled use and track that result
            playhist[0] += 1
            output = guesses[0]
        else:
            # otherwise just make a random one
            output = random.choice("RPS")
    else:
        # if no noise, then randomly choose among the best choices
        # (there is usually just one but not always)
        winner = random.choice(choices)
        playhist[winner] += 1
        output = guesses[winner]

    myhist.pop(0)
    youhist.pop(0)

myhist.append(output)