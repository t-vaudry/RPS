import math, random

def voyATenerSuerte():
    opciones = []
    maxMojo = 0
    for key in mojo_dict.keys():
        if mojo_dict[key] > maxMojo:
            maxMojo = mojo_dict[key]
            opciones = [key]
        elif mojo_dict[key] == maxMojo:
            opciones.append(key)
    return random.choice(opciones)

def mojo(ganador, perdedor):
    mojoGanador = mojo_dict[ganador]
    mojoPerdedor = mojo_dict[perdedor]
    diferenciaMojos = mojoGanador - mojoPerdedor
    exp = (diferenciaMojos * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    nuevo_mojoGanador = round(mojoGanador + (k * (1 - odds)))
    nueva_diferenciaMojos = nuevo_mojoGanador - mojoGanador
    nuevo_mojoPerdedor = mojoPerdedor - nueva_diferenciaMojos
    if nuevo_mojoPerdedor < 1:
        nuevo_mojoPerdedor = 1
    mojo_dict[ganador] = int(nuevo_mojoGanador)
    mojo_dict[perdedor] = int(nuevo_mojoPerdedor)

if input=='':
    mojo_dict = {'R':500, 'P':500, 'S':500}
    mejorOpcion = {'R':'P','P':'S','S':'R'}
    k = 1
else:
    mojo(mejorOpcion[input], input)

output = voyATenerSuerte()