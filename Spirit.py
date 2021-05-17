class Spirit:
    orientacion="este"
    coordenadaM=1
    coordenadaN=1
    def __init__(self,orientacion,coordenadaM,coordenadaN):
        self.orientacion=orientacion
        self.coordenadaM=coordenadaM
        self.coordenadaN=coordenadaN

    def nuevaCoordenada(self,x,y):
        self.coordenadaM=x
        self.coordenadaN=y

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