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
    if(action == "W"):
        if(to == "R"):
            return "P"
        if(to == "P"):
            return "S"
        if(to == "S"):
            return "R"
    if(action == "L"):
        if(to == "R"):
            return "S"
        if(to == "P"):
            return "R"
        if(to == "S"):
            return "P"
    if(action =="D"):
        return to

class Modelo:
    def __init__(self, cantidadCaracts):
        self.cantidadCaracts = cantidadCaracts
        self.contextos = {}
        self.contextoActual=""
    #agrega char al contexto actual
    def agregarChar(self, c):
        self.contextoActual+=c
        
        if( len(self.contextoActual) > self.cantidadCaracts):
            pos =len(self.contextoActual)-self.cantidadCaracts
            self.contextoActual = self.contextoActual[pos:]
            
        if(len(self.contextoActual) == self.cantidadCaracts):
            if not (self.contextoActual in self.contextos):
                self.contextos[self.contextoActual] = {}
            if c in self.contextos[self.contextoActual]:
		self.contextos[self.contextoActual][c] += 1
	    else:
		self.contextos[self.contextoActual][c] = 1
		
    def mostrar(self):
        for contexto,tabla in self.contextos.iteritems():
            for label,cantidad in tabla.iteritems():
                print "en ctx "+contexto+" N("+label+")="+str(cantidad)
        print "--------------------------"
        
        
    #escupe la posibilidad del char segun el contexto actual
    
    def probabilidad(self,c):
        if not self.contextoActual in self.contextos:
            return 0;

        
        total = 0
        for letra, veces in self.contextos[self.contextoActual].iteritems():
            total += veces
        if(c in self.contextos[self.contextoActual]):
            return self.contextos[self.contextoActual][c]/total
        else:
            return 0
    
    #escupe el char mas posible segun el contexto actualizado
    def proximoMasProbable(self):
        masprobable="W"
        mascantidad=0
        for label in self.contextos[self.contextoActual]:
            cantidad =self.contextos[self.contextoActual][label]
            if cantidad>mascantidad:
                masprobable=label
                mascantidad=cantidad
                
        return masprobable
    
class MultiModel:
    def __init__(self, max_model):
        self.models=[]
        for i in range(0,max_model-1):
            self.models.append(Modelo(i+1))

    def agregarChar(self,c):
        for m in self.models:
            m.agregarChar(c)

    def probabilidad(self, c):#es un promedio
        p=0
        for m in self.models:
           p+=m.probabilidad(c)

        p/=len(self.models)
        
        return p
    def proximoMasProbable(self):
        posibles=["R","P","S"]#SOLO ANDA CON RPS!
        masprobable="R"
        masprobabilidad=0
        for label in posibles:
            probabilidad =self.probabilidad(label)
            if probabilidad > masprobabilidad:
                masprobabilidad = probabilidad
                masprobable = label
                
        return masprobable
    
        
initialize = 1
if(input==""):
    prevInput="caca"
    modelo1=Modelo(1)
    modelo2=Modelo(2)
    initialize = 0
    multiModelo=MultiModel(7)
    
if(input !=""):
    inputReal = input#myResult(input, prevInput)
    #input = whatDoes(inputReal, prevInput)

    multiModelo.agregarChar(inputReal)
    modelo1.agregarChar(inputReal)
    modelo2.agregarChar(inputReal)
    
    #modelo1.mostrar()
    masprobable = multiModelo.proximoMasProbable()#modelo1.proximoMasProbable()
    output = masprobable#whatDoes(masprobable, prevInput)
    
    
    #output = whatDoes("W", "R")






if(input==""):
    modelo1 = Modelo(1)
    prevInput ="R"#asumo que el anterior fue roca porque es mejor
    output="R"
else:
    prevInput = input