#!/usr/bin/python
import random

#CONSTANTES
ROCK = "R"
PAPER = "P"
SCISSOR = "S"
MODELOS = 50
WIN = {ROCK:PAPER,SCISSOR:ROCK,PAPER:SCISSOR}

#IMPLEMENTACION

#Actualizo todos los modelos con la informacion que me provee el input respecto a todas las keys anteriores
#Aca deberia crear todo lo necesario tambien?
def actualizar_modelos(modelos, n, input, key):
	for index in range(n):
		modelo = modelos[index]
		if index == 0:
			modelo[input] += 1
		else:
			new_key = key[-index:]
			if new_key in modelo:
				modelo[new_key][input] += 1
			else:
				modelo[new_key] = {ROCK:1, PAPER:1, SCISSOR:1}

def weighted_choice(choices):
   total = sum(w for c, w in choices.items())
   r = random.uniform(0, total)
   upto = 0
   for c, w in choices.items():
      if upto + w >= r:
         return c
      upto += w
 
if input == "":
	n = 0
	record = []
	modelos = []
	modelo_0 = {ROCK:1, PAPER:1, SCISSOR:1}
	modelos.append(modelo_0)


	his_play = random.choice(["R","P","S"])

else:
	if n > MODELOS:
		m_index = MODELOS
	else:
		m_index = n
		modelos.append({})
	key = ''.join(record)[-m_index:]
	actualizar_modelos(modelos,m_index,input,key)

	record.append(input)
	found = False;
	key = ''.join(record)[-m_index:]
	
	
	while not found:		
		if key not in modelos[m_index]: 
			m_index-=1
			if m_index > 0:
				key = key[-m_index:]
			else:
				dic = modelos[m_index]
				found = True
			continue
		else:
			dic = modelos[m_index][key]
			found = True
	his_play = weighted_choice(dic)

my_play = WIN[his_play]
output = my_play
n += 1