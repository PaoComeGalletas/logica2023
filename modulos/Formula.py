from modulos.Clausula import Clausula


class Formula:

    def __init__(self):
        self.clausules=[]
        self.certificado={}

    def addClausule(self, clausule):
        self.clausules.append(clausule)

    def __str__(self):
        names = []
        for c in self.clausules:
            names.append(str(c))
        return '[' + ' '.join(names) + ']'


    def orFormula(self, formula):
        f=Formula()
        for ca in self.clausules:
            for cb in formula.clausules:
                c=ca.getClone()
                for a in cb.atomos.values():
                    c.addAtom(a.getClone())
                f.addClausule(c)

        return f

    def notFormula(self):
        f= []
        for c in self.clausules:
            fa=Formula()
            for a in c.atomos.values():
                a=a.getClone()
                a.negar()
                ca=Clausula()
                ca.addAtom(a)
                fa.addClausule(ca)
            f.append(fa)
        while len(f) > 1:
            a=f.pop(0)
            b=f.pop(0)
            f.insert(0, a.orFormula(b))
        return f.pop()



    def andFormula(self, formula):
        f=Formula()
        for c in self.clausules:
            f.addClausule(c.getClone())
        for c in formula.clausules:
            f.addClausule(c.getClone())
        return f