#!/usr/bin/python
import math
import random

#CONSTANTES
ROCK = "R"
PAPER = "P"
SCISSOR = "S"
MODELOS = 10

#IMPLEMENTACION

#Actualizo todos los modelos con la informacion que me provee el input respecto a todas las keys anteriores
#Aca deberia crear todo lo necesario tambien?
def actualizar_modelos(modelos, n, input, key):
	for index in range(n):
		modelo = modelos[index]
		if index == 0:
			modelo[input] += 1
		else:
			modelo[key[-index:]][input] += 1

def define_his_play1(dic):
	max_value = 0
	for play,value in dic.items():
		if value > max_value:
			max_value = value
			his_play = [play]
		elif value == max_value:
			his_play.append(play)
	his_play = random.choice(his_play) #Si hay mas de una con el mismo valor, decide una random de esas
	return his_play

def my_play(his_play):
	if his_play == "R":
		my_play = "P"
	elif his_play == "P":
		my_play = "S"
	else:
		my_play = "R"
	return my_play

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
			modelos[m_index][key] = {ROCK:1, PAPER:1, SCISSOR:1} 
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
	his_play = define_his_play1(dic)

output = my_play(his_play)
n += 1