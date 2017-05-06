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
   hist=[[0]*3]*2
   eval=[0]*3
   flag=[False]*2
   subs=[[0]*3]*2
   prin=[[[0]*3]*2]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   for i in range(4):
       x=0
       y=0
       for j in range(2):
           for k in range(3):
               if prin[i][j][k]>prin[i][x][y]:
                  x=j
                  y=k
       if flag[x]:
          re=mdl(subs[x][y]-k2i[input])
          if re==2:
             meta[i]-=1
          else:
             meta[i]+=re
   for j in range(2):
       for k in range(3):
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
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=-1
   j=min(5,len(tRNA))
   while i<0 and j>1:
         j-=1
         RNA=tRNA[-j:]
         DNA=mRNA[-j:]
         i=tRNA.find(RNA,0,-1)
   while i>=0:
         if mRNA[i:(i+j-1)]==DNA:
            hist[0][k2i[tRNA[i+j]]]+=1
         hist[1][k2i[tRNA[i+j]]]+=1
         i=tRNA.find(RNA,i+1,-1)
   flag[0]=(hist[0][0]<>hist[0][1] or hist[0][1]<>hist[0][2])
   flag[1]=(hist[1][0]<>hist[1][1] or hist[1][1]<>hist[1][2])
   if flag[0]:
      for i in range(3):
          eval[i]=hist[0][mdl(i-1)]-hist[0][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[0][i]=mdl(j-i)
   if flag[1]:
      for i in range(3):
          eval[i]=hist[1][mdl(i-1)]-hist[1][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[1][i]=mdl(j-i)
   output=random.choice("RPS")
   i=meta.index(max(meta))
   if max(meta)>0:
      x=0
      y=0
      for j in range(2):
          for k in range(3):
              if prin[i][j][k]>prin[i][x][y]:
                 x=j
                 y=k
   if flag[x] and prin[i][x][y]>0:
      output=i2k[subs[x][y]]