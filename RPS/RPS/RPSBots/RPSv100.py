import random

def mdl(m):
    m%=3
    if m<0:
       m+=3
    return m

if not input:
   hist=[[[[[0]*3]*3]*3]*3]*3
   prin=[[0]*4]*3
   subs=[0]*3
   meta=[0]*4
   eval=[0]*3
   c2i={'R':0,'P':1,'S':2}
   i2c={0:'R',1:'P',2:'S'}
   flag=False
   N=0
   c=random.choice("RPS")
else:
   N+=1
   if N==1:
      z=input
      b=c
      c=random.choice("RPS")
   elif N==2:
      y=z
      z=input
      a=b
      b=c
      c=random.choice("RPS")
   elif N==3:
      x=y
      y=z
      z=input
      hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][c2i[z]]+=1
      a=b
      b=c
      c=random.choice("RPS")
   else:

      if flag:
         for j in range(4):
             M=prin[0][j]
             k=0
             for i in range(1,3):
                 if prin[i][j]>M:
                    M=prin[i][j]
                    k=i
             re=mdl(subs[k]-c2i[z])
             if re==2:
                meta[j]-=1
             else:
                meta[j]+=re
         for i in range(3):
             prin[i][1]*=0.9
             prin[i][3]*=0.9
             re=mdl(subs[i]-c2i[z])
             if re==0:
                for j in range(2,4):
                    prin[i][j]-=0.1
             elif re==1:
                for j in range(4):
                    prin[i][j]+=1
             elif re==2:
                for j in range(2):
                    prin[i][j]-=1
                for j in range(2,4):
                    prin[i][j]*=0.5

      x=y
      y=z
      z=input
      hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][c2i[z]]+=1

      t=random.choice([0,1,2])
      flag=((hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][0]<>hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][1]) or
            (hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][1]<>hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][2]))

      if flag:
         for i in range(3):
             eval[i]=hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][mdl(i-1)]-hist[c2i[a]][c2i[x]][c2i[b]][c2i[y]][mdl(i+1)]
         j=eval.index(max(eval))
         for i in range(3):
             subs[i]=mdl(j-i)
         M=max(meta)
         j=meta.index(M)
         if M>0:
            M=prin[0][j]
            k=0
            for i in range(1,3):
                if prin[i][j]>M:
                   M=prin[i][j]
                   k=i
            if M>0:
               t=subs[k]

      a=b
      b=c
      c=i2c[t]

output=c