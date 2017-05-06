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
   flag=[False]*5
   hist=[[0]*3]*2
   eval=[0]*3
   subs=[[0]*6]*5
   prin=[[[0]*6]*7]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   for i in range(4):
       x=0
       y=0
       for j in range(5):
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
   for j in range(5):
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
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=-1
   j=min(5,len(DNA))
   while i<0 and j>1:
         j-=1
         RNA=DNA[-j:]
         i=DNA.find(RNA,0,-1)
   if i<0:
      for k in range(len(DNA)):
          hist[0][d0s[DNA[k]]]+=1
          hist[1][d1s[DNA[k]]]+=1
   while i>=0:
         hist[0][d0s[DNA[i+j]]]+=1
         hist[1][d1s[DNA[i+j]]]+=1
         i=DNA.find(RNA,i+1,-1)
   flag[0]=((hist[0][0]<>hist[0][1] or hist[0][1]<>hist[0][2]) and
            (hist[1][0]<>hist[1][1] or hist[1][1]<>hist[1][2]))
   if flag[0]:
      for i in range(3):
          eval[i]=hist[0][mdl(i-1)]-hist[0][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[0][i]=mdl(j-i)
      for i in range(3):
          eval[i]=hist[1][mdl(i-1)]-hist[1][mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          subs[0][i+3]=mdl(j-i+1)
   for i in range(2):
       j=min((2-i),len(DNA))
       RNA=tRNA[-j:]
       x=tRNA.rfind(RNA,0,-1)
       y=tRNA.find(RNA,0,-1)
       flag[2*i+1]=(x>=0)
       flag[2*i+2]=(y>=0)
       if flag[2*i+1]:
          x=mdl(k2i[tRNA[x+j]]+1)
          for k in range(3):
              subs[2*i+1][k]=mdl(x-k)
       if flag[2*i+2]:
          y=mdl(k2i[tRNA[y+j]]+1)
          for k in range(3):
              subs[2*i+2][k]=mdl(y-k)
   for i in range(2):
       j=min((2-i),len(DNA))
       RNA=mRNA[-j:]
       x=mRNA.rfind(RNA,0,-1)
       y=mRNA.find(RNA,0,-1)
       flag[2*i+1]=flag[2*i+1] and (x>=0)
       flag[2*i+2]=flag[2*i+2] and (y>=0)
       if flag[2*i+1]:
          x=mdl(k2i[mRNA[x+j]]-1)
          for k in range(3):
              subs[2*i+1][k+3]=mdl(x-k+1)
       if flag[2*i+2]:
          y=mdl(k2i[mRNA[y+j]]-1)
          for k in range(3):
              subs[2*i+2][k+3]=mdl(y-k+1)
   output=random.choice("RPS")
   i=meta.index(max(meta))
   if max(meta)>0:
      x=0
      y=0
      for j in range(5):
          for k in range(6):
              if prin[i][j][k]>prin[i][x][y]:
                 x=j
                 y=k
      if flag[x] and prin[i][x][y]>0:
         output=i2k[subs[x][y]]