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
   flag=[False]*2
   hist=[[0]*3]*2
   eval=[0]*3
   subs=[0]*2
   prin=[0]*2
   meta=[[0]*3]*2
   output=random.choice("RPS")
else:
   for i in range(2):
       if flag[i]:
          prin[i]*=0.9
          for j in range(3):
              eval[j]=0
          eval[mdl(subs[i]+1)]+=meta[i][0]
          eval[subs[i]]+=meta[i][1]
          eval[mdl(subs[i]-1)]+=meta[i][2]
          j=mdl(eval.index(max(eval))-k2i[input])
          if j==2:
             prin[i]-=1
          else:
             prin[i]+=j
          meta[i][mdl(subs[i]-k2i[input])]+=1
   DNA+=kon[input+output]
   output=random.choice("RPS")
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=min(100,len(DNA))
   j=-1
   k=1
   while i>1 and j<0:
         i-=1
         RNA=DNA[-i:]
         j=DNA.find(RNA,0,-1)
   while j>=0:
         hist[0][d0s[DNA[i+j]]]+=k
         hist[1][d1s[DNA[i+j]]]+=k
         j=DNA.find(RNA,j+1,-1)
         k+=0.1
   for i in range(2):
       flag[i]=(hist[i][0]<>hist[i][1] or hist[i][1]<>hist[i][2])
       if flag[i]:
          for j in range(3):
              eval[j]=hist[i][mdl(j-1)]-hist[i][mdl(j+1)]
          j=eval.index(max(eval))
          subs[i]=mdl(i+j)
   i=prin.index(max(prin))
   if flag[i] and prin[i]>0:
      for j in range(3):
          eval[j]=0
      eval[mdl(subs[i]+1)]+=meta[i][0]
      eval[subs[i]]+=meta[i][1]
      eval[mdl(subs[i]-1)]+=meta[i][2]
      output=i2k[eval.index(max(eval))]