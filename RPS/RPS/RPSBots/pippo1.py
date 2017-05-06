import random
#sopralapancalacapracapmasottolapancalacapracrepa
out = random.randrange(10)
out1=random.randrange(10)
out2=random.randrange(10)
print(out, out1, out2)
final=(out1+out2+out)%3
if final==0:
    output='R'
elif final==1:
    output='P'
else:
    output='S'