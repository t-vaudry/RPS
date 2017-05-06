def whatDoes(action,to):
    if(action == 'W'):
        if(to == 'R'):
            return 'P'
        if(to == 'P'):
            return 'S'
        if(to == 'S'):
            return 'R'
    if(action == 'L'):
        if(to == 'R'):
            return 'S'
        if(to == 'P'):
            return 'R'
        if(to == 'S'):
            return 'P'
    if(action =='D'):
        return to
    return "caca"

output = whatDoes('W','R')