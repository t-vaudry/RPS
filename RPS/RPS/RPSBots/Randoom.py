import random
beats={'S':'R','P':'S','R':'P'}
opponentIsGarbage=True
if input=='':
    output=random.choice(['R','P','S'])
else:
    output=random.choice([beats[input],input])