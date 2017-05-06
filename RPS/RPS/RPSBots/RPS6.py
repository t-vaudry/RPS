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
   flag=[False]*4
   subs=[[0]*6]*4
   prin=[[[0]*6]*4]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   for i in range(4):
       x=0
       y=0
       for j in range(4):
           for k in range(6):
               if prin[i][j][k]>prin[i][x][y]:
                  x=j
                  y=k
       if flag[x]:
          y=mdl(subs[x][y]-k2i[input])
          if y==2:
             meta[i]-=1
          else:
             meta[i]+=y
   for j in range(4):
       if flag[j]:
          for k in range(6):
             prin[1][j][k]*=0.9
             prin[3][j][k]*=0.9
             y=mdl(subs[j][k]-k2i[input])
             if y==0:
                for i in range(2,4):
                    prin[i][j][k]-=0.1
             elif y==1:
                for i in range(4):
                    prin[i][j][k]+=1
             elif y==2:
                for i in range(4):
                    if i<2 or prin[i][j][k]<2:
                       prin[i][j][k]-=1
                    else:
                       prin[i][j][k]*=0.5
   DNA+=kon[input+output]
   i=min(10,len(DNA))
   k=-1
   while i>1 and k<0:
         i-=1
         RNA=DNA[-i:]
         k=DNA.rfind(RNA,0,-1)
   flag[0]=(k>=0)
   if flag[0]:
      for j in range(3):
          subs[0][j]=mdl(d0s[DNA[i+k]]-j+1)
      for j in range(3):
          subs[0][j+3]=mdl(d1s[DNA[i+k]]-j-1)
   i=min(5,len(DNA))
   k=-1
   while i>1 and k<0:
         i-=1
         RNA=DNA[-i:]
         k=DNA.rfind(RNA,0,-1)
   flag[1]=(k>=0)
   if flag[1]:
      for j in range(3):
          subs[1][j]=mdl(d0s[DNA[i+k]]-j+1)
      for j in range(3):
          subs[1][j+3]=mdl(d1s[DNA[i+k]]-j-1)
   i=min(3,len(DNA))
   k=-1
   while i>1 and k<0:
         i-=1
         RNA=DNA[-i:]
         k=DNA.rfind(RNA,0,-1)
   flag[2]=(k>=0)
   if flag[2]:
      for j in range(3):
          subs[2][j]=mdl(d0s[DNA[i+k]]-j+1)
      for j in range(3):
          subs[2][j+3]=mdl(d1s[DNA[i+k]]-j-1)
   i=min(2,len(DNA))
   k=-1
   while i>1 and k<0:
         i-=1
         RNA=DNA[-i:]
         k=DNA.rfind(RNA,0,-1)
   flag[3]=(k>=0)
   if flag[3]:
      for j in range(3):
          subs[3][j]=mdl(d0s[DNA[i+k]]-j+1)
      for j in range(3):
          subs[3][j+3]=mdl(d1s[DNA[i+k]]-j-1)
   output=random.choice("RPS")
   i=meta.index(max(meta))
   if max(meta)>0:
      x=0
      y=0
      for j in range(3):
          for k in range(6):
              if prin[i][j][k]>prin[i][x][y]:
                 x=j
                 y=k
      if flag[x] and prin[i][x][y]>0:
         output=i2k[subs[x][y]]