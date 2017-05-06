#!/usr/bin/env python
#no uso RPS sino WLD (win-lose-draw),
#asumo que el otro programa esta respondiendo a mi input
#WLD se calcula relativo a su input inmediato anterior

def myResult(myInput, hisInput):
    if(myInput == "R"):
        if(hisInput == "R"):
            return "D"
        if(hisInput == "P"):
            return "L"
        if(hisInput == "S"):
            return "W"
    if(myInput == "P"):
        if(hisInput == "R"):
            return "W"
        if(hisInput == "P"):
            return "D"
        if(hisInput == "S"):
            return "L"
    if(myInput == "S"):
        if(hisInput == "R"):
            return "L"
        if(hisInput == "P"):
            return "W"
        if(hisInput == "S"):
            return "D"

def whatDoes(action,to):
    if(action == 'W'):
        if(to == 'R'):
            return 'P'
        if(to == 'P'):
            return 'S'
        if(to == 'S'):
            return 'R'
    if(action == 'L'):
        if(to == 'R'):
            return 'S'
        if(to == 'P'):
            return 'R'
        if(to == 'S'):
            return 'P'
    if(action =='D'):
        return to

class Modelo:
    def __init__(self, cantidadCaracts):
        self.cantidadCaracts = cantidadCaracts
        self.contextos = {}
        self.contextoActual=""
    #agrega char al contexto actual
    def agregarChar(self, c):
        if(len(self.contextoActual) == self.cantidadCaracts):
            if(self.contextos[self.contextoActual]==nil):
               self.contextos[self.contextoActual] = {"W":0, "L":0, "D":0}
            self.contextos[contextoActual][char] += 1
        print c
        #self.contextoActual += c
        if( len(self.contextoActual) > self.cantidadCaracts):
            self.contextoActual = self.contextoActual[:cantidadCaracts]
    #escupe la probabilidad de que venga char dado el contexto actual
    def probabilidadSiguiente(self, c):
        return self.contextos[self.contextoActual][c]

initialize = 1
if(input==""):
    prevInput="caca"
    modelo1=Modelo(1)
    initialize = 0
    
if(input !=""):
    inputReal = myResult(input, prevInput)
    #input = whatDoes(inputReal, prevInput)
    """
    modelo1.agregarChar(input)
    opciones=["W","D","L"]
    masprobable="W"
    for c in opciones:
        if(modelo1.probabilidadSiguiente(c)>modelo1.probabilidadSiguiente(masprobable)):
            masprobable = c
    """

    """
    masProbable = "W"
    traduccion = whatDoes(masProbable, prevInput)
    output = whatDoes("W", traduccion)
    """
    output = whatDoes("W", "R")






if(input==""):
    modelo1 = Modelo(1)
    prevInput ="R"#asumo que el anterior fue roca porque es mejor
    output="R"
else:
    prevInput = input