#!/usr/bin/python
import random

#CONSTANTES
ROCK = "R"
PAPER = "P"
SCISSOR = "S"
MODELOS = 40
WIN = {ROCK:PAPER,SCISSOR:ROCK,PAPER:SCISSOR}

#IMPLEMENTACION
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
				modelo[new_key] = {ROCK:0, PAPER:0, SCISSOR:0}
				modelo[new_key][input] += 1

def define_his_play1(dic):
	max_value = 0
	his_play = []
	for play,value in dic.items():
		if value > max_value:
			max_value = value
			his_play = [play]
		elif value == max_value:
			his_play.append(play)
	his_play = random.choice(his_play) #Si hay mas de una con el mismo valor, decide una random de esas
	return his_play

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
	his_play = define_his_play1(dic)

my_play = WIN[his_play]
output = my_play
n += 1