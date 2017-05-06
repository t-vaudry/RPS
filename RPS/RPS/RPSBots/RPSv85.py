import random

kon={'RR':'1','RP':'2','RS':'3','PR':'4','PP':'5','PS':'6','SR':'7','SP':'8','SS':'9'}
d0s={'1':0,'2':0,'3':0,'4':1,'5':1,'6':1,'7':2,'8':2,'9':2}
d1s={'1':0,'2':1,'3':2,'4':0,'5':1,'6':2,'7':0,'8':1,'9':2}
k2i={'R':0,'P':1,'S':2}
i2k={0:'R',1:'P',2:'S'}

def mdl(N):
    N%=3
    if N<0:
       N+=3
    return N

if not input:
   DNA=""
   mRNA=""
   tRNA=""
   flag=[False]*13
   hist=[[0]*3]*2
   eval=[0]*3
   subs=[[0]*6]*13
   prin=[[[0]*6]*13]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   for i in range(4):
       x=0
       y=0
       for j in range(13):
           for k in range(6):
               if prin[i][j][k]>prin[i][x][y]:
                  x=j
                  y=k
       if flag[x]:
          re=mdl(subs[x][y]-k2i[input])
          if re==2:
             meta[i]-=1
          else:
             meta[i]+=re
   for j in range(13):
       for k in range(6):
           prin[1][j][k]*=0.9
           prin[3][j][k]*=0.9
           if flag[j]:
              re=mdl(subs[j][k]-k2i[input])
              if re==0:
                 for i in range(2,4):
                     prin[i][j][k]-=0.1
              elif re==1:
                 for i in range(4):
                     prin[i][j][k]+=1
              elif re==2:
                 for i in range(4):
                     if i<2 or prin[i][j][k]<2:
                        prin[i][j][k]-=1
                     else:
                        prin[i][j][k]*=0.5
   tRNA+=input
   mRNA+=output
   DNA+=kon[input+output]
   hist[0][k2i[input]]+=1
   hist[1][k2i[output]]+=1
   for i in range(4):
       j=min((4-i),len(DNA))
       RNA=DNA[-j:]
       k=DNA.rfind(RNA,0,-1)
       flag[i]=(k>=0)
       if flag[i]:
          x=mdl(d0s[DNA[k+j]]+1)
          y=mdl(d1s[DNA[k+j]]-1)
          for k in range(3):
              subs[i][k]=mdl(x-k)
          for k in range(3):
              subs[i][k+3]=mdl(y-k+1)
   for i in range(4):
       j=min((4-i),len(DNA))
       RNA=tRNA[-j:]
       k=tRNA.rfind(RNA,0,-1)
       flag[i+4]=(k>=0)
       if flag[i+4]:
          x=mdl(k2i[tRNA[k+j]]+1)
          y=mdl(k2i[mRNA[k+j]]-1)
          for k in range(3):
              subs[i+4][k]=mdl(x-k)
          for k in range(3):
              subs[i+8][k+3]=mdl(y-k+1)
   for i in range(4):
       j=min((4-i),len(DNA))
       RNA=mRNA[-j:]
       k=mRNA.rfind(RNA,0,-1)
       flag[i+8]=flag[i+4] and (k>=0)
       flag[i+4]=flag[i+8]
       if flag[i+8]:
          x=mdl(k2i[tRNA[k+j]]+1)
          y=mdl(k2i[mRNA[k+j]]-1)
          for k in range(3):
              subs[i+8][k]=mdl(x-k)
          for k in range(3):
              subs[i+4][k+3]=mdl(y-k+1)
   flag[12]=((hist[0][0]<>hist[0][1] or hist[0][1]<>hist[0][2]) and
             (hist[1][0]<>hist[1][1] or hist[1][1]<>hist[1][2]))
   if flag[12]:
      for i in range(3):
          eval[i]=hist[0][mdl(i-1)]-hist[0][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[12][i]=mdl(j-i)
      for i in range(3):
          eval[i]=hist[1][mdl(i-1)]-hist[1][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[12][i+3]=mdl(j-i+1)
   output=random.choice("RPS")
   i=meta.index(max(meta))
   if max(meta)>0:
      x=0
      y=0
      for j in range(13):
          for k in range(6):
              if prin[i][j][k]>prin[i][x][y]:
                 x=j
                 y=k
      if flag[x] and prin[i][x][y]>0:
         output=i2k[subs[x][y]]