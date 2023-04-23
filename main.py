import re

from modulos.Atomo import Atomo
from modulos.Clausula import Clausula
from modulos.Formula import Formula
import copy

class Prioridad:

    lista=[]

    def __init__(self, lista):
        self.lista=lista

    def imprimir(self):

        for i in self.lista:
            if i[0].isalpha():
                print(f"{i} Es operando ")
            elif self.getpriority(i) == -1:
                print("(")
            elif self.getpriority(i) == -2:
                print(")")
            else:
                print(f"{i} Es operador y tiene prioridad {self.getpriority(i)}")

    def getpriority(self, oper):
        if oper == "|":
            return 1
        if oper == "&":
            return 2
        if oper == ">":
            return 3
        if oper == "=":
            return 4
        if oper == "-":
            return 5
        if oper == "(":
            return -1
        if oper == ")":
            return -2
        else:
            return 0


def getPrioridad(oper):
    if oper == "|":
        return 1
    if oper == "&":
        return 2
    if oper == ">":
        return 3
    if oper == "=":
        return 4
    if oper == "-":
        return 5
    if oper == "(":
        return -1
    if oper == ")":
        return -2
    else:
        return 0



def infijo2posfijo(infijo):
    posfijo = []
    pila = []

    for ch in infijo:
        p=getPrioridad(ch)
        if p == -1: #-----------CASO PARENTESIS ABRIERO --------------
            pila.append(ch)
        elif p == -2: #-----------CASO PARENTESIS CERRADO --------------
            while len(pila) > 0:
                tope=pila.pop()
                if(tope != "("):
                    posfijo.append(tope)
                else:
                    break
        elif p > 0: #---------SI ES OPERADOR---------
            if len(pila)==0 or p> getPrioridad(pila[-1]):
                pila.append(ch)
            else:
                while len(pila) > 0 and p < getPrioridad(pila[-1]):
                    tope=pila.pop()
                    posfijo.append(tope)

                pila.append(ch)
        else: #---------SI ES OPERANDO--------------
            posfijo.append(ch)

    while len(pila) > 0: #-----------AGREGAMOS AL POSTFIJO LO QUE QUEDO EN LA PILA------------------
        posfijo.append(pila.pop())

    return posfijo

def evaluarPostfijo(postfijo):
    pila=[]
    for ch in postfijo:
        p=getPrioridad(ch)
        if p==0:
            a=Atomo(ch)
            c=Clausula()
            f=Formula()
            c.addAtom(a)
            f.addClausule(c)
            pila.append(f)
        elif p == 1: # -----OR-----
            b= pila.pop()
            a=pila.pop()
            c.orFormula(b)
            pila.append(c)
        elif p == 2: #---------------AND---------
            b= pila.pop()
            a=pila.pop()
            c=a.andFormula(b)
            pila.append(c)
        elif p == 3: #---------------IMPLICA---------
            b= pila.pop()
            a=pila.pop()
            c=a.notFormula().orFormula(b)
            pila.append(c)
        elif p==4: #------------Si y solo si
            b=pila.pop()
            a=pila.pop()
            c=a.notFormula().orFormula(b)
            d= b.notFormula().orFormula(a)
            e=c.andFormula(d)
            pila.append(e)
        elif p ==5: #------------NOT-----------
            a=pila.pop()
            a=a.notFormula()
            pila.append(a)



        #for a in pila:
            # print(a)
        #print('')
    return pila.pop()



pattern = r'\||&|>|=|~|\(|\)|\w+'
archivo=open("data/formula1.txt")
lines=archivo.readlines()
infijo=[]
for line in lines:
    infijo=re.findall(pattern,line)

#formula=Formula()
#formula.addClausule(cla)


print(infijo) #-----IMPRIMIENTO EL INFIJO-----
postfijo=infijo2posfijo(infijo)
print(postfijo)
formula=evaluarPostfijo(postfijo)
print(formula)



#---------------IMPRIMIR PRIORIDADES Y SI ES OPERADOR U OPERANDO------------------

#p=Prioridad(lista)
#p.imprimir()
