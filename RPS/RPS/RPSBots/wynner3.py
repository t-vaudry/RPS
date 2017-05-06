import random

if input=='':
   hy=["R","P","S"]
   count=0
if input=='R':
   ex=['R']*random.randint(1,5)
   hy.extend(ex)
elif input=='P':
   hy.extend(['S'])
else:
   hy.extend(['P'])
output = random.choice(hy)
if count %7 ==0:
   hy.pop(-1)
count +=1