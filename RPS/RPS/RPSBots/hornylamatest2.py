if input=="":
    beats={'R':'P', 'P':'S', 'S':'R'}
    last='R'

else:
    last=input
    
output=beats[beats[last]]