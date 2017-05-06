import random

def mdl(N):
    N%=3
    if N<0:
       N+=3
    return N

if not input:
   comb={'RR':'1','RP':'2','RS':'3','PR':'4','PP':'5','PS':'6','SR':'7','SP':'8','SS':'9'}
   splt={'1':0,'2':1,'3':2,'4':0,'5':1,'6':2,'7':0,'8':1,'9':2}
   k2i={'R':0,'P':1,'S':2}
   i2k={0:'R',1:'P',2:'S'}
   hist=[0]*3
   eval=[0]*3
   prin=[0]*3
   meta=[0]*3
   DNA=""
   flag=False
   output=random.choice("RPS")
else:
   DNA+=comb[output+input]
   if flag:
      for i in range(3):
          meta[i]*=0.9
          re=mdl(prin[i]-k2i[input])
          if re==2:
             meta[j]-=1
          else:
             meta[j]+=re
   i=-1
   j=min(5,len(DNA))
   while i<0 and j>1:
         j-=1
         RNA=DNA[-j:]
         i=DNA.find(RNA,0,-1)
   while i>=0:
         hist[splt[DNA[i+j]]]+=1
         i=DNA.find(RNA,i+1,-1)
   output=random.choice("RPS")
   flag=(hist[0]<>hist[1]) or (hist[1]<>hist[2])
   if flag:
      for i in range(3):
          eval[i]=hist[mdl(i-1)]-hist[mdl(i+1)]
      j=eval.index(max(eval))
      for i in range(3):
          prin[i]=mdl(j-i)
      M=max(meta)
      if M>0:
         output=i2k[prin[meta.index(M)]]