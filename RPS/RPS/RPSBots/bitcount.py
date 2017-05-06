import random

if input=="":
    count=random.randint(0,2147483647)
bc=count
count+=1
bc=(bc&0x55555555)+(bc>>1)
bc=(bc&0x33333333)+(bc>>2)
bc=(bc&0x0f0f0f0f)+(bc>>4)
bc=(bc&0x00ff00ff)+(bc>>8)
bc=(bc&0x0000ffff)+(bc>>16)
output=["R","P","S"][bc%3]