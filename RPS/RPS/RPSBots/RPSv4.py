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
   hist=[[0]*3]*2
   eval=[[0]*3]*2
   subs=[0]*6
   prin=[[0]*6]*4
   meta=[0]*4
   DNA=""
   flag=False
   output=random.choice("RPS")
else:
   DNA+=com[output+input]
   if flag:
      for i in range(4):
          j=prin[i].index(max(prin[i]))
          re=mdl(subs[j]-k2i[input])
          if re==2:
             meta[j]-=1
          else:
             meta[j]+=re
      for j in range(6):
          prin[1][j]*=0.9
          prin[3][j]*=0.9
          re=mdl(subs[j]-k2i[input])
          if re==0:
             for i in range(2,4):
                 prin[i][j]-=0.1
          elif re==1:
             for i in range(4):
                 prin[i][j]+=1
          elif re==2:
             for i in range(4):
                 if i<2 or prin[i][j]<2:
                    prin[i][j]-=1
                 else:
                    prin[i][j]*=0.5
   for i in range(2):
       for j in range(3):
           hist[i][j]=0
   i=-1
   j=min(5,len(DNA))
   while i<0 and j>1:
         j-=1
         RNA=DNA[-j:]
         i=DNA.find(RNA,0,-1)
   while i>=0:
         hist[0][ego[DNA[i+j]]]+=1
         hist[1][idt[DNA[i+j]]]+=1
         i=DNA.find(RNA,i+1,-1)
   output=random.choice("RPS")
   flag=((hist[0][0]<>hist[0][1] or hist[0][1]<>hist[0][2]) and
         (hist[1][0]<>hist[1][1] or hist[1][1]<>hist[1][2]))
   if flag:
      for i in range(2):
          for j in range(3):
              eval[i][j]=hist[i][mdl(j-1)]-hist[i][mdl(j+1)]
      j=eval[0].index(max(eval[0]))
      for i in range(3):
          subs[i]=mdl(j-i)
      j=eval[1].index(max(eval[1]))
      for i in range(3):
          subs[i+3]=mdl(j-i)
      i=meta.index(max(meta))
      if max(meta)>0:
         j=prin[i].index(max(prin[i]))
         if max(prin[i])>0:
            output=i2k[subs[j]]