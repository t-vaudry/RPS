#!/usr/bin/env python
#no uso RPS sino WLD (win-lose-draw),
#asumo que el otro programa esta respondiendo a mi input
#WLD se calcula relativo a su input inmediato anterior
import random
import math
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

        if(len(self.contextoActual) == self.cantidadCaracts):
            if not (self.contextoActual in self.contextos):
                self.contextos[self.contextoActual] = {}
            if c in self.contextos[self.contextoActual]:
		self.contextos[self.contextoActual][c] += 1
	    else:
		self.contextos[self.contextoActual][c] = 1
		
        self.contextoActual+=c
        
        if( len(self.contextoActual) > self.cantidadCaracts):
            pos =len(self.contextoActual)-self.cantidadCaracts
            self.contextoActual = self.contextoActual[pos:]
            
        
		
    def mostrar(self):
        for contexto,tabla in self.contextos.iteritems():
            for label,cantidad in tabla.iteritems():
                print "en ctx "+contexto+" N("+label+")="+str(cantidad)
        print "--------------------------"
        
    def valido(self):
        return self.contextoActual in self.contextos
    #escupe la posibilidad del char segun el contexto actual
    
    def probabilidad(self,c):
        if not self.contextoActual in self.contextos:
            return 0;

        
        total = 0
        for letra, veces in self.contextos[self.contextoActual].iteritems():
            total += veces
        if(c in self.contextos[self.contextoActual]):
            ret = float(self.contextos[self.contextoActual][c])/total
            return ret
        else:
            return 0
    
    #escupe el char mas posible segun el contexto actualizado
    def proximoMasProbable(self):
        if not self.contextoActual in self.contextos:
            return "R";
        
        masprobable="R"
        mascantidad=0.0
        for label in self.contextos[self.contextoActual]:
            cantidad =self.contextos[self.contextoActual][label]
            if cantidad>mascantidad:
                masprobable=label
                mascantidad=cantidad
        #print "soy "+str(self.cantidadCaracts)+" y creo que va a salir "+masprobable
        #print "contexto: "+self.contextoActual
        #self.mostrar()
        
        return masprobable
    
class MultiModel:
    def __init__(self, max_model, simbolos):
        self.models=[]
        for i in range(0,max_model):
            self.models.append(Modelo(i+1))
        self.weights=[1.0 for i in range(max_model)]
        self.simbolos=simbolos

    def aprenderRPS(self, jugada_enemigo):
        
        for i in range(len(self.models)):
            modelo=self.models[i]
            previsto = modelo.proximoMasProbable()
            enviado=whatDoes("W",previsto)
            if enviado==whatDoes("W",jugada_enemigo):
                self.weights[i]+=1
            if enviado==whatDoes("D",jugada_enemigo):
                self.weights[i]-=0.5
            if enviado==whatDoes("L",jugada_enemigo):
                self.weights[i]-=2

            if(self.weights[i]<1):
                self.weights[i]=1
            #if previsto==whatDoes("

    def agregarChar(self,c):
        for m in self.models:
            m.agregarChar(c)
            
    def mostrar(self):
        mejor=0
        print "-----------------------"
        #for i in range(len(self.weights)):
            #self.models[i].mostrar()
        for i in range(len(self.weights)):
            print "weight: "+str(self.weights[i])+" at:"+str(i)
        #print "el que mas me gusta es "+ str(mejor)
        
    def probabilidad(self, c):#es un promedio
        p=0.0
        total = 0.0
        #print "votamos la letra "+c
        for i in range(len(self.models)):
            m = self.models[i]
            a=len(self.models)
            w = self.weights[i]
            if m.valido():
                #print str(i) +" dice que " + str(m.probabilidad(c)*w)+" desde el contexto " + m.contextoActual
                p+=m.probabilidad(c)*w
                total +=1*w
            """
            
            w = 1#self.weights[i]
            if m.valido():
                total += w
                dp=m.probabilidad(c)*w
                p+=dp
            """
                
        if total == 0:
            return 0
        return p/total
    
    def proximoMasProbable(self):
        posibles=self.simbolos#SOLO ANDA CON RPS!
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
    prevoutput="R"
    initialize = 0
    multiModelo=MultiModel(50,["R","P","S"])
    
if(input !=""):
    inputReal = input#myResult(input, prevInput)
    #input = whatDoes(inputReal, prevInput)
    multiModelo.aprenderRPS(inputReal)
    multiModelo.agregarChar(inputReal)
    
    #modelo1.agregarChar(inputReal)
    #modelo2.agregarChar(inputReal)
    
    #modelo1.mostrar()
    masprobable = multiModelo.proximoMasProbable()#modelo1.proximoMasProbable()
    #multiModeloRes.agregarChar(myResult(prevoutput,inputReal))
    #accionMasProbable=multiModeloRes.proximoMasProbable()
    #recontraProbable=whatDoes(accionMasProbable,masprobable)
    #output = whatDoes("L", recontraProbable)
    output = whatDoes("W", masprobable)
    #print "mas probable: " + masprobable
    #multiModelo.mostrar()
    #print "malo dice" + input +" bueno dice "+prevoutput
    prevoutput = output


if(input==""):
    modelo1 = Modelo(1)
    prevInput ="R"#asumo que el anterior fue roca porque es mejor
    output="R"
else:
    prevInput = input