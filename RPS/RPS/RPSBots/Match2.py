#-----------
#RPS Match2
#-----------
#---Programmed by Dracux---
#For isladelmono.com.ar

option=["R","P","S"]
input=""
output=""

def whokills(selection):
    if selection=="R":
        retorno="P"
    if selection=="P":
        retorno="S"
    if selection=="S":
        retorno="R"
    return retorno

def nextmove(Selection):
    if selection=="R":
        retorno="S"
    if selection=="S":
        retorno="P"
    if selection=="P":
        retorno="R"
    return retorno

def whowon(yours,his):
    #Empate sigo tomandolo como ganado.
    ganado=False
    if yours=="R":
        if his!="P":
            ganado=True
    if yours=="P":
        if his!="S":
            ganado=True
    if yours=="S":
        if his!="R":
            ganado=True
    return ganado

lastPlayed=""
winner=True
if input=="":
    actualPlay="R"
    output=actualPlay
else:
    winner=whowon(output,input)
    if winner==False:
        actualPlay=nextmove(actualPlay)
        output=actualPlay