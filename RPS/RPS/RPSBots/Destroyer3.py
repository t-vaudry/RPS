import random

def minus(lis,el):
       res = []
       for e in lis:
              if e != el:
                     res += e
       return res

if input == '':
       r = 0
       p = 0
       s = 0
       output = random.choice(['R','P','S'])
else:
       if input == 'R':
              r += 1
       if input == 'S':
              s += 1
       else:
              p += 1
       remainders = ['R','P','S']
       if r > p or r > s:
              remainders = minus(remainders,['R'])
       if p > r or p > s:
              remainders = minus(remainders,['P'])
       if s > r or s > p:
              remainders = minus(remainders,['S'])
       output = remainders[0]