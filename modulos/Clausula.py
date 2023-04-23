from modulos.Atomo import Atomo

class Clausula:

    def __init__(self):
        self.atomos={}

    def addAtom(self, atomo):
        self.atomos[atomo]=atomo

    def getClone(self):
        c= Clausula()
        for a in self.atomos:
            c.addAtom(a.getClone())
        return c

    def getNOTClone(self):
        c = Clausula()
        for a in self.atomos:
            c.addAtom(a.getClone())
        return c

    def __str__(self):
        names = []
        for atom in self.atomos.values():
            names.append(str(atom))
        return '('+'|'.join(names)+')'