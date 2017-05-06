import random

if input=="":
    count=random.randint(0,2147483647)
bc=count
count+=1
bc=(bc&0x55555555)+(bc&0xaaaaaaaa>>1)
bc=(bc&0x33333333)+(bc&0xcccccccc>>2)
bc=(bc&0x0f0f0f0f)+(bc&0xf0f0f0f0>>4)
bc=(bc&0x00ff00ff)+(bc&0xff00ff00>>8)
bc=(bc&0x0000ffff)+(bc&0xffff0000>>16)
output=["R","P","S"][bc%3]