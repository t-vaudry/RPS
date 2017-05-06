import random

def mdl(N):
    N%=3
    if N<0:
       N+=3
    return N

if not input:
   com={'RR':'1','RP':'2','RS':'3','PR':'4','PP':'5','PS':'6','SR':'7','SP':'8','SS':'9'}
   ego={'1':0,'2':1,'3':2,'4':0,'5':1,'6':2,'7':0,'8':1,'9':2}
   idt={'1':0,'2':0,'3':0,'4':1,'5':1,'6':1,'7':2,'8':2,'9':2}
   k2i={'R':0,'P':1,'S':2}
   i2k={0:'R',1:'P',2:'S'}
   hist=[[0]*2]*3
   eval=[[0]*2]*3
   subs=[0]*6
   prin=[[0]*4]*6
   meta=[0]*4
   DNA=""
   flag=False
   output=random.choice("RPS")
else:
   DNA+=com[output+input]
   if flag:
      for j in range(4):
          M=prin[0][j]
          k=0
          for i in range(1,6):
              if prin[i][j]>M:
                 M=prin[i][j]
                 k=i
          re=mdl(subs[k]-k2i[input])
          if re==2:
             meta[j]-=1
          else:
             meta[j]+=re
      for i in range(6):
          prin[i][1]*=0.9
          prin[i][3]*=0.9
          re=mdl(subs[i]-k2i[input])
          if re==0:
             for j in range(2,4):
                 prin[i][j]-=0.1
          elif re==1:
             for j in range(4):
                 prin[i][j]+=1
          elif re==2:
             for j in range(4):
                 if (j<2 or prin[i][j]<2):
                    prin[i][j]-=1
                 else:
                    prin[i][j]*=0.5
   for i in range(3):
       for j in range(2):
           hist[i][j]=0
   i=-1
   j=min(5,len(DNA))
   while i<0 and j>1:
         j-=1
         RNA=DNA[-j:]
         i=DNA.find(RNA,0,-1)
   while i>=0:
         hist[ego[DNA[i+j]]][0]+=1
         hist[idt[DNA[i+j]]][1]+=1
         i=DNA.find(RNA,i+1,-1)
   output=random.choice("RPS")
   flag=(((hist[0][0]<>hist[1][0]) or (hist[1][0]<>hist[2][0])) and
         ((hist[0][1]<>hist[1][1]) or (hist[1][1]<>hist[2][1])))
   if flag:
      for i in range(3):
          for j in range(2):
              eval[i][j]=hist[mdl(i-1)][j]-hist[mdl(i+1)][j]
      M=eval[0][0]
      j=0
      for i in range(1,3):
          if eval[i][0]>eval[j][0]:
             j=i
      if ((eval[mdl(j+1)][0]==M or eval[mdl(j-1)][0]==M) and random.choice([0,1])==0):
         j=mdl(j+1)
      else:
         j=mdl(j-1)
      for i in range(3):
          subs[i]=mdl(j-i)
      M=eval[0][1]
      j=0
      for i in range(1,3):
          if eval[i][1]>eval[j][1]:
             j=i
      if ((eval[mdl(j+1)][1]==M or eval[mdl(j-1)][1]==M) and random.choice([0,1])==0):
         j=mdl(j+1)
      else:
         j=mdl(j-1)
      for i in range(3):
          subs[i]=mdl(j-i)
      M=max(meta)
      j=meta.index(M)
      if M>0:
         M=prin[0][j]
         k=0
         for i in range(1,6):
             if prin[i][j]>M:
                M=prin[i][j]
                k=i
         if M>0:
            output=i2k[subs[k]]