
class Atomo:

    def __init__(self, name):
        self.name=name
        self.state=True
        self.tuple=()

    def negar(self):
        self.state=not(self.state)

    def getClone(self):
        a= Atomo(self.name)
        a.state=self.state
        return a

    def getNOTClone(self):
        a = Atomo(self.name)
        a.state = not(self.state)
        return a

    def __str__(self):
        if self.state:
            return self.name
        else:
            #tuple=list(tuple)
            #self.name="~"+self.name
            return f"~{self.name}"