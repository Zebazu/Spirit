from Matriz import Matriz
from Terreno import Terreno
from Spirit import Spirit

class Tablero:

    def __init__(self,Spirit,Matriz):
        self.spirit = Spirit
        self.matriz = Matriz
        self.mtsPorSegundo = 0

spirit = Spirit("norte",0,0)
matriz = Matriz(2,2)
matriz.generarArea()

Tablero_game = Tablero(spirit,matriz)