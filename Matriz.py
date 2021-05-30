from Terreno import Terreno
import random
import numpy as np

class Matriz:

    def __init__(self,n,m):
        self.matrix =  np.empty((n, m), dtype=object)

    def generarArea(self):
        #Implementar aleatorio para crear terrenos

        for n in range (np.shape(self.matrix)[0]):
            for m in range (np.shape(self.matrix)[1]):

                #Generar terreno aleatorio
                tipoGenerado = random.choice([0,1])
                obstaculoGenerado = [random.choice([0,1]),random.choice([0,1]),random.choice([0,1]),random.choice([0,1])]
                self.matrix[n][m] = Terreno(tipoGenerado,obstaculoGenerado)
                
        
        nObjetivo = random.randrange(np.shape(self.matrix)[0])
        mObjetivo = random.randrange(np.shape(self.matrix)[1])

        self.matrix[nObjetivo][mObjetivo].asignarTerrenoObjetivo()

X = Matriz(1,2)
X.generarArea()

