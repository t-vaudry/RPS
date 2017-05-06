input = 'S'
try:
    last
except:
    from random import choice
    output = choice(list('RPS'))
    last = ''
else:
    if last == input:
        choices = {'R':'P','P':'S','S':'R'}
        output = choices[input]
    else:
        choices = {'PR':'P','PS':'S','RS':'R'}
        key = ''.join(sorted('RPS'.replace(input,'')))
        last = input
        output = choices[key]
print output