import random

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
def listaMax(unHash):
    mayor = -1
    keys = []
    for key in unHash.keys():
        if unHash[key] > mayor:
            keys =[]
            keys.append(key)
            mayor = unHash[key]
        elif unHash[key] == mayor: 
            keys.append(key)
    return keys
def predecir(ctx):
    if m1[ctx]['R'] == m1[ctx]['S'] and m1[ctx]['P'] == m1[ctx]['S']:
        predicciones = listaMax(m0)
        return predicciones,True
    else:
        predicciones = listaMax(m1[ctx])
        return predicciones,False
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
    predicciones,llegoANivelCero = predecir(buffer[1])
    buffer.pop(0)
    output = ganarleA(random.choice(predicciones))