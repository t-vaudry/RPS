import random

k2i={'R':0,'P':1,'S':2}
i2k={0:'R',1:'P',2:'S'}

def mdl(N):
    N%=3
    if N<0:
       N+=3
    return N

if not input:
   mRNA=""
   tRNA=""
   flag=[False]*2
   hist=[[0]*3]*2
   eval=[0]*3
   subs=[0]*6
   prin=[[0]*6]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   for i in range(4):
       j=prin[i].index(max(prin[i]))
       if (j<3 and flag[0]) or (j>3 and flag[1]):
          k=mdl(subs[j]-k2i[input])
          if k==2:
             meta[i]-=1
          else:
             meta[i]+=k
   for j in range(6):
       if (j<3 and flag[0]) or (j>3 and flag[1]):
          prin[1][j]*=0.9
          prin[3][j]*=0.9
          k=mdl(subs[j]-k2i[input])
          if k==0:
             for i in range(2,4):
                 prin[i][j]-=0.1
          elif k==1:
             for i in range(4):
                 prin[i][j]+=1
          elif k==2:
             for i in range(4):
                 if i<2 or prin[i][j]<2:
                    prin[i][j]-=1
                 else:
                    prin[i][j]*=0.5
   tRNA+=input
   mRNA+=output
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=-1
   j=min(5,len(tRNA))
   while i<0 and j>1:
         j-=1
         RNA=tRNA[-j:]
         DNA=mRNA[-j:]
         i=tRNA.rfind(RNA,0,-1)
   if i<0:
      for j in range(len(tRNA)):
          hist[0][k2i[tRNA[j]]]+=j+1
   while i>0 and mRNA[i:(i+j-1)]<>DNA:
         hist[0][k2i[tRNA[i+j]]]+=1
         i=tRNA.rfind(RNA,0,i+j-2)
   if i>=0:
      if mRNA[i:(i+j-1)]==DNA:
         hist[0][k2i[tRNA[i+j]]]+=2
      else:
         hist[0][k2i[tRNA[i+j]]]+=1
   i=-1
   j=min(5,len(mRNA))
   while i<0 and j>1:
         j-=1
         RNA=mRNA[-j:]
         DNA=tRNA[-j:]
         i=mRNA.rfind(RNA,0,-1)
   if i<0:
      for j in range(len(mRNA)):
          hist[1][k2i[mRNA[j]]]+=j+1
   while i>0 and tRNA[i:(i+j-1)]<>DNA:
         hist[1][k2i[mRNA[i+j]]]+=1
         i=mRNA.rfind(RNA,0,i+j-2)
   if i>=0:
      if tRNA[i:(i+j-1)]==DNA:
         hist[1][k2i[mRNA[i+j]]]+=2
      else:
         hist[1][k2i[mRNA[i+j]]]+=1
   flag[0]=(hist[0][0]<>hist[0][1] or hist[0][1]<>hist[0][2])
   flag[1]=(hist[1][0]<>hist[1][1] or hist[1][1]<>hist[1][2])
   if flag[0]:
      for i in range(3):
          eval[i]=hist[0][mdl(i-1)]-hist[0][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[i]=mdl(j-i)
   if flag[1]:
      for i in range(3):
          eval[i]=hist[1][mdl(i-1)]-hist[1][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[i+3]=mdl(j-i+1)
   output=random.choice("RPS")
   i=meta.index(max(meta))
   if max(meta)>0:
      j=prin[i].index(max(prin[i]))
      if ((j<3 and flag[0]) or (j>3 and flag[1])) and max(prin[i])>0:
         output=i2k[subs[j]]