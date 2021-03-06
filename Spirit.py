class Spirit:

    def __init__(self,orientacion,coordenadaM,coordenadaN):
        self.orientacion=orientacion
        self.coordenadaI=coordenadaM
        self.coordenadaJ=coordenadaN

    def nuevaCoordenada(self,i,j):
        self.coordenadaI=i
        self.coordenadaJ=j

    def nuevaOrientacion(self,orientacion):
        self.orientacion=orientacion

    def giroPositivo(self):
        if self.orientacion=="este":
            self.orientacion="norte"
        if self.orientacion=="norte":
            self.orientacion="oeste"
        if self.orientacion=="oeste":
            self.orientacion="sur"
        if self.orientacion=="sur":
            self.orientacion="este"
    def giroNegativo(self):
        if self.orientacion=="este":
            self.orientacion="sur"
        if self.orientacion=="sur":
            self.orientacion="oeste"
        if self.orientacion=="oeste":
            self.orientacion="norte"
        if self.orientacion=="norte":
            self.orientacion="este"

    def getCoordenadaI(self):
        return self.coordenadaI
    
    def getCoordenadaJ(self):
        return self.coordenadaJ
    
    def flechaOrientacion(self):
        if self.orientacion=="este":
            return "→"
        if self.orientacion=="norte":
            return "↑"
        if self.orientacion=="oeste":
            return "←"
        if self.orientacion=="sur":
            return "↓"
