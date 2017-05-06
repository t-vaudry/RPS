import math, random, datetime

def choice():
    opciones = []
    maxMojo = 0
    for key in mojo_dict.keys():
        if mojo_dict[key] > maxMojo:
            maxMojo = mojo_dict[key]
    for key in mojo_dict.keys():
        if mojo_dict[key] == maxMojo:
            opciones.append(key)
    return random.choice(opciones)

def mojo(ganador, perdedor):
    mojoGanador = mojo_dict[ganador]
    mojoPerdedor = mojo_dict[perdedor]
    diferenciaMojos = mojoGanador - mojoPerdedor
    exp = (diferenciaMojos * - 1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    nuevo_mojoGanador = round(mojoGanador + (prop['k'] * (1 - odds)))
    nueva_diferenciaMojos = nuevo_mojoGanador - mojoGanador
    nuevo_mojoPerdedor = mojoPerdedor - nueva_diferenciaMojos
    mojo_dict[ganador] = int(nuevo_mojoGanador)
    mojo_dict[perdedor] = int(nuevo_mojoPerdedor)

def mix():
    if (prop['iter'] > prop['numSameStrategy']):
        mojo_dict['R'] = defaultInitValue
        mojo_dict['S'] = defaultInitValue
        mojo_dict['P'] = defaultInitValue
        prop['iter'] = 0
        prop['k'] = random.randint(0,2)
        prop['numSameStrategy'] = random.randint(1,25)
    else:
        prop['iter'] += 1

if not input:
    defaultInitValue = 1000
    prop = {'iter': 0, 'k': 0, 'numSameStrategy': 100}
    mojo_dict = {'R':defaultInitValue,'P':defaultInitValue,'S':defaultInitValue}
    winner = {'R':'P','P':'S','S':'R'}
    random.seed(datetime.datetime.now())
else:
    mojo(winner[input], input)
    mix()

output = choice()