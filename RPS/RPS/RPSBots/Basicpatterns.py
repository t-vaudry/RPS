if not input:
    beat={'R':'P','P':'S','S':'R','':'S'}
    output='S'
    last=''
    records={'R':{'R':0,'P':0,'S':0},'P':{'R':0,'P':0,'S':0},'S':{'R':0,'P':0,'S':0}}
else:
    if last:
        records[last][input]=records[last][input]+1
        maxv=0
        maxk=''
        for k, v in records[input].items():
            if v>maxv:
                maxv=v
                maxk=k
        output=beat[maxk]
    else:
        output=beat[input]
    last=input