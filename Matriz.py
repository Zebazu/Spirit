from Terreno import Terreno
import random
import numpy as np

class Matriz:

    def __init__(self,n,m):
        self.matrix =  np.empty((n, m), dtype=object)
        self.dimensionN = n
        self.dimensionM = m

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
        while(nObjetivo==0 and mObjetivo==0):
            nObjetivo = random.randrange(np.shape(self.matrix)[0])
            mObjetivo = random.randrange(np.shape(self.matrix)[1])

        self.matrix[nObjetivo][mObjetivo].asignarTerrenoObjetivo()
    
    def generarAreaDefinidaTXT(self):
        archivo = open("matrix.txt","r")
        fila = 0
        for linea in archivo :
            
            fields = linea.split("/")
            for n in range (len(fields)):
                
                celda = fields[n].split(";")

                #Si la celda contiene el objetivo
                if(int(celda[2])==1):
                    
                    #Extraemos el tipo de terreno
                    tipoTerreno = int(celda[0])
                    #Extraemos los obstaculos
                    obstaculosTerreno = list(map(int, celda[1].split(",")))

                    self.matrix[fila][n] = Terreno(tipoTerreno ,obstaculosTerreno)
                    self.matrix[fila][n].asignarTerrenoObjetivo()
                    #print("El objetivo esta en "+str(fila)+" "+str(n))
                
                else:
                    #Extraemos el tipo de terreno
                    tipoTerreno = int(celda[0])
                    #Extraemos los obstaculos
                    obstaculosTerreno = list(map(int, celda[1].split(",")))

                    self.matrix[fila][n] = Terreno(tipoTerreno ,obstaculosTerreno)
                    #print("Posicion  ["+str(fila)+","+str(n))
                
                #coordenada fila y n es columna
            fila+=1
    
    def getTerreno(self,i,j):
        return self.matrix[i][j]
    
    def getDimensionN(self):
        return self.dimensionN 

    def getDimensionM(self):
        return self.dimensionM

Matrixtest = Matriz(6,8)
Matrixtest.generarAreaDefinidaTXT()
