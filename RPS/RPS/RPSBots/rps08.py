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
   flag=False
   hist=[[0]*3]*2
   eval=[0]*3
   subs=[0]*6
   prin=[[0]*6]*4
   meta=[0]*4
   output=random.choice("RPS")
else:
   if flag:
      for i in range(4):
          k=mdl(subs[prin[i].index(max(prin[i]))]-k2i[input])
          if k==2:
             meta[i]-=1
          else:
             meta[i]+=k
      for j in range(6):
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
   DNA+=kon[input+output]
   output=random.choice("RPS")
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=min(115,len(DNA))
   j=-1
   while i>1 and j<0:
         i-=1
         RNA=DNA[-i:]
         j=DNA.find(RNA,0,-1)
   flag=(j>=0)
   p=1
   while j>=0:
         hist[0][d0s[DNA[i+j]]]+=p
         hist[1][d1s[DNA[i+j]]]+=p
         j=DNA.find(RNA,j+1,-1)
         p+=0.1
   if flag:
      for i in range(2):
          for j in range(3):
              eval[j]=hist[i][mdl(j-1)]-hist[i][mdl(j+1)]
          k=eval.index(max(eval))
          for j in range(3):
              subs[3*i+j]=mdl(k-j+i)
      i=meta.index(max(meta))
      if meta[i]>0:
         j=prin[i].index(max(prin[i]))
         if prin[i][j]>0:
            output=i2k[subs[j]]