def ganarleA(jugada):
    if jugada == 'R':
        return 'P'
    if jugada == 'P':
        return 'S'
    if jugada == 'S':
        return 'R'
def actualizarModelo(ctx, jugada, llegoAmcero):
    if ctx == '':
        m0[jugada] += 1
    else:
        m1[ctx][jugada] += 1
        if llegoAmcero:
            m0[jugada] += 1
def predecir(ctx):
    if m1[ctx]['R'] == m1[ctx]['S'] and m1[ctx]['P'] == m1[ctx]['S']:
        prediccion = max(m0.iterkeys(), key=(lambda key: m0[key]))
        return prediccion,True
    else:
        prediccion = max(m1[ctx].iterkeys(), key=(lambda key: m1[ctx][key]))
        return prediccion,False
if input == '': 
    output = 'R'
    m0 = {
        'R' : 0,
        'S' : 0,
        'P' : 0
    }
    m1 = {
        'R' : {
            'R' : 0,
            'S' : 0,
            'P' : 0
        },
        'S' : {
            'R' : 0,
            'S' : 0,
            'P' : 0
        },
        'P' : {
            'R' : 0,
            'S' : 0,
            'P' : 0
        }    
    }
    niveles = {
        'm0' : m0,
        'm1' : m1
    }
    buffer = ['']
    llegoANivelCero = False
else:
    buffer.append(input)
    actualizarModelo(buffer[0],buffer[1],llegoANivelCero)
    prediccion,llegoANivelCero = predecir(buffer[1])
    buffer.pop(0)
    output = ganarleA(prediccion)