import random
import copy
def ganarleA(jugada):
    if jugada == 'R':
        return 'P'
    if jugada == 'P':
        return 'S'
    if jugada == 'S':
        return 'R'
        
def actualizarModelo(buffer, nivelesVisitados):
    for nivel in range(0,5):
        if nivelesVisitados[nivel]:
            mx = niveles[str(nivel)]
            if(nivel == 0):
                mx[buffer[4]] += 1
            if(nivel == 1):
                mx[buffer[3]][buffer[4]] += 1
            if(nivel == 2):
                mx[buffer[2]][buffer[3]][buffer[4]] += 1
            if(nivel == 3):
                mx[buffer[1]][buffer[2]][buffer[3]][buffer[4]] += 1
            if(nivel == 4):
                mx[buffer[0]][buffer[1]][buffer[2]][buffer[3]][buffer[4]] += 1
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

def valuesSonIguales(unHash):
    return unHash['R'] == unHash['S'] and unHash['P'] == unHash['S']
        
def predecir(ctx):
    contexto = list(ctx)
    nivelesAccedidos = [False]*5
    nivelesAccedidos[4] = True
    for i in range (0,4):
        if not contexto[i]:
            contexto[i] = 'R'
    if valuesSonIguales(m4[contexto[0]][contexto[1]][contexto[2]][contexto[3]]):
        nivelesAccedidos[3] = True
        if valuesSonIguales(m3[contexto[1]][contexto[2]][contexto[3]]):
            nivelesAccedidos[2] = True
            if valuesSonIguales(m2[contexto[2]][contexto[3]]):
                nivelesAccedidos[1] = True
                if valuesSonIguales(m1[contexto[3]]):
                    nivelesAccedidos[0] = True
                    predicciones = listaMax(m0)
                else:
                    predicciones = listaMax(m1[contexto[3]])
            else:
                predicciones = listaMax(m2[contexto[2]][contexto[3]])
        else:
            predicciones = listaMax(m3[contexto[1]][contexto[2]][contexto[3]])
    else:
        predicciones = listaMax(m4[contexto[0]][contexto[1]][contexto[2]][contexto[3]])
    for i in range (0,4):
        if not ctx[i]:
            nivelesAccedidos[4-i] = False
    return predicciones,nivelesAccedidos
if input == '': 
    output = 'R'
    m0 = {
    'R' : 0,
    'S' : 0,
    'P' : 0
    }
    m1 = {
        'R' : copy.deepcopy(m0),
        'S' : copy.deepcopy(m0),
        'P' : copy.deepcopy(m0)    
    }
    m2 = {
        'R' : copy.deepcopy(m1),
        'S' : copy.deepcopy(m1),
        'P' : copy.deepcopy(m1)    
    }
    m3 = {
        'R' : copy.deepcopy(m2),
        'S' : copy.deepcopy(m2),
        'P' : copy.deepcopy(m2)    
    }
    m4 = {
        'R' : copy.deepcopy(m3),
        'S' : copy.deepcopy(m3),
        'P' : copy.deepcopy(m3)    
    }
    niveles = {
        '0' : m0,
        '1' : m1,
        '2' : m2,
        '3' : m3,
        '4' : m4
    }
    buffer = [False]*4
    buffer.append('')
    nivelesVisitados = [False] * 5
else:
    buffer.append(input)
    actualizarModelo(buffer,nivelesVisitados)
    buffer.pop(0)
    predicciones,nivelesVisitados = predecir(buffer)    
    output = ganarleA(random.choice(predicciones))