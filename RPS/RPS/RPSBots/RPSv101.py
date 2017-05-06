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
   flag=False
   N=0
   c=random.choice([0,1,2])
else:
   N+=1
   if N<4:
      if N>2:
         x=y
      if N>1:
         y=z
      z=c2i[input]
      if N>2:
         hist[a][x][b][y][z]+=1
      if N>1:
         a=b
      b=c
      c=random.choice([0,1,2])
   else:
      if flag:
         for j in range(4):
             M=prin[0][j]
             k=0
             for i in range(1,3):
                 if prin[i][j]>M:
                    M=prin[i][j]
                    k=i
             re=mdl(subs[k]-z)
             if re==2:
                meta[j]-=1
             else:
                meta[j]+=re
         for i in range(3):
             prin[i][1]*=0.9
             prin[i][3]*=0.9
             re=mdl(subs[i]-z)
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
      z=c2i[input]
      hist[a][x][b][y][z]+=1
      for i in range(3):
          eval[i]=hist[a][x][b][y][mdl(i-1)]-hist[a][x][b][y][mdl(i+1)]
      flag=((eval[0]<>eval[1]) or (eval[1]<>eval[2]))
      a=b
      b=c
      c=random.choice([0,1,2])
      if flag:
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
               c=subs[k]
if c==0:
   output="R"
elif c==1:
   output="P"
elif c==2:
   output="S"