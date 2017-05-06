'''
Created on 5 Jun 2015

@author: naji
'''
'''
Created on 16 Feb 2015

@author: naji
'''
import random as ran
fmatch = True
chis = []
phis = []
n = 0
rtimesc = 0
ptimesc = 0
stimesc = 0
rtimesp = 0
ptimesp = 0
stimesp = 0
def inv(i):
    o = ''
    if i == 'R':
        o = 'P'
    elif i == 'P':
        o = 'S'
    elif i == 'S':
        o = 'R'
    return o
# IO
i = input
o = ''
if i == 'R':
    rtimesp += 1
elif i == 'P':
    ptimesp += 1
elif i == 'S':
    stimesp += 1
else:
    Exception("Error!")
    # Fmatch and Nmatch
if fmatch:
    # First match?
    ro = ran.randint(0,2)
    if ro == 0:
        o = 'R'
        rtimesc += 1
    elif ro == 1:
        o = 'P'
        ptimesc += 1
    else:
        o = 'S'
        stimesc += 1
else:
    # n Match?  
    if i in phis:
        o = inv(phis[len(phis)-1])
    else:
        if i in chis:
            o = inv(chis[len(chis)-1])
        else:
            if rtimesp == rtimesc:
                o = inv('R')
            elif ptimesp == ptimesc:
                o = inv('P')
            elif stimesp == stimesc:
                o = inv('S')
            else:
                if rtimesp == n:
                    o = 'R'
                elif ptimesp == n:
                    o = 'P'
                elif stimesp == n:
                    o = 'S'
                else:
                    fn = n % 3
                    if fn == 0:
                        o = 'R'
                    elif fn == 1:
                        o = 'P'
                    else:
                        o = 'S'
# Increment | Print | Store | Set fmatch to False
output = o
n  += 1
phis.append(i)
chis.append(o)
fmatch = False
print(n)