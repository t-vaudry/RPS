import math, random, datetime

def choice():
    opciones = []
    maxMojo = 0
    for key in mojo_dict.keys():
        if round(mojo_dict[key]) > maxMojo:
            maxMojo = round(mojo_dict[key])
    for key in mojo_dict.keys():
        if round(mojo_dict[key]) == maxMojo:
            opciones.append(key)
    return random.choice(opciones)

def mojo(ganador, perdedor):
    mojoGanador = mojo_dict[ganador]
    mojoPerdedor = mojo_dict[perdedor]
    diferenciaMojos = mojoGanador - mojoPerdedor
    exp = (diferenciaMojos * - 1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    nuevo_mojoGanador = mojoGanador + (prop['k'] * (1 - odds))
    nueva_diferenciaMojos = nuevo_mojoGanador - mojoGanador
    nuevo_mojoPerdedor = mojoPerdedor - nueva_diferenciaMojos
    mojo_dict[ganador] = nuevo_mojoGanador
    mojo_dict[perdedor] = nuevo_mojoPerdedor

if not input:
    defaultInitValue = 1000
    prop = {'iter': 0, 'k': 0.01}
    mojo_dict = {'R':defaultInitValue,'P':defaultInitValue,'S':defaultInitValue}
    winner = {'R':'P','P':'S','S':'R'}
    random.seed(datetime.datetime.now())
else:
    if (input != output):
        if (winner[input] == output):
            mojo(output, input)
        else: 
            mojo(input, output)

output = choice()