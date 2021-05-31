from Matriz import Matriz
from Spirit import Spirit

#pip install --user XlsxWriter
import xlsxwriter
  

class Tablero:

    def __init__(self,Spirit,Matriz):
        self.spirit = Spirit
        self.matriz = Matriz
        self.mtsPorSegundo = 0
        self.workbook = xlsxwriter.Workbook('Tablero.xlsx')
        self.worksheet = None
    
    #Funcion que permite exportar el tablero dentro de un archivo xlsx llamado "Tablero"
    def exportarTableroExcel(self):
        self.workbook = xlsxwriter.Workbook('Tablero.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        
        #Inicio de ciclos for para recorrer la matriz que contiene objetos tipo Terreno
        for n in range (self.matriz.getDimensionN()):
            for m in range (self.matriz.getDimensionM()):
                
                #Obtenemos un bloque de terreno de posición [n,m]
                bloqueTerreno = self.matriz.getTerreno(n,m)
                
                #Inicializamos el formato de celda para la hoja excel utilizando el bloque de terreno previo
                cell_format1 = formatoTerreno(bloqueTerreno,self.workbook)

                #Establecemos la posición que tendra en la hoja Excel de manera ajustada
                fila = int(n)+4
                columna = colToExcel(m+3)
                posicionCelda = str(columna)+str(fila)
                
                #Si coincide con el spirit, se marcará con una flecha en la casilla para mostrar su posición
                if (self.spirit.getCoordenadaI() ==  int(n)) and (self.spirit.getCoordenadaJ() == int(m)):
                    cell_format1.set_align('center')
                    cell_format1.set_bold()
                    orientacionSpirit = self.spirit.flechaOrientacion()
                    self.worksheet.write(posicionCelda, orientacionSpirit,cell_format1)

                #Caso contrario se marcará el terreno de forma normal
                else:
                    self.worksheet.write(posicionCelda, '',cell_format1)

       

        self.workbook.close()

    
#Funcion que convierte un valor numerico a valor alfabetico de columna de Excel
#Fuente: shorturl.at/uLZ19
#colToExcel(6) -> F
def colToExcel(col): 
    excelCol = str()
    div = col 
    while div:
        (div, mod) = divmod(div-1, 26) 
        excelCol = chr(mod + 65) + excelCol
    return excelCol

#Funcion que permite darle formato a una celda [i,j] utilizando los atributos del terreno
def formatoTerreno(Terreno,workbook):
    cell_format1 = workbook.add_format() 

    #Tipo
    if(Terreno.getTipoTerreno() ==  0):
        cell_format1.set_bg_color('FFDBBD')
    else:
        cell_format1.set_bg_color('B53430')

    #Obstaculos
    for i in range(4):
        if Terreno.getObstaculosTerreno()[i] == 1 and i == 0:
            #Obstaculo Superior
            cell_format1.set_top(5)
            cell_format1.set_top_color('black')

        elif Terreno.getObstaculosTerreno()[i] == 1 and i == 1:
            #Obstaculo Costado Derecho
            cell_format1.set_right(5)
            cell_format1.set_right_color('black')

        elif Terreno.getObstaculosTerreno()[i] == 1 and i == 2:
            #Obstaculo Inferior
            cell_format1.set_bottom(5)
            cell_format1.set_bottom_color('black')

        elif Terreno.getObstaculosTerreno()[i] == 1 and i == 3:
            #Obstaculo Costado Izquierdo
            cell_format1.set_left(5)
            cell_format1.set_left_color('black')
    
    #Objetivo
    if (Terreno.esObjetivo()):
        cell_format1.set_diag_border(2)
        cell_format1.set_diag_type(3)

    return cell_format1
        


tiempo=0.0
m=0
n=0
contadorOrigen=0

def find_next(spirit,coordinates, maze, visitados):
    global tiempo
    next_coordinates = []
    lista=maze.getTerreno(coordinates[0], coordinates[1]).getDetalleObstaculo().split(";")
    print(lista)
    if(maze.getTerreno(coordinates[0],coordinates[1]).getDetalleTerreno()=="Terreno Llano"):
        tiempo += 2
    else:
        tiempo +=0.833
    if (spirit.orientacion == "este"):
        if coordinates[0] + 1 < m and not ("Derecho" in lista):

            next_coordinates.append((coordinates[0] + 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] + 1 < n and not ("Inferior" in lista):
            spirit.nuevaOrientacion("sur")
            visitados.append("giro")
            tiempo+=4
            next_coordinates.append((coordinates[0], coordinates[1] + 1))
            return spirit, next_coordinates
        elif coordinates[0] - 1 >= 0 and not ("Izquierdo" in lista):
            spirit.nuevaOrientacion("oeste")
            visitados.append("giro")
            visitados.append("giro")
            tiempo+=8
            next_coordinates.append((coordinates[0] - 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] - 1 >= 0 and not ("Superior" in lista):
            spirit.nuevaOrientacion("norte")
            visitados.append("giro")
            visitados.append("giro")
            visitados.append("giro")
            tiempo+=12
            next_coordinates.append((coordinates[0], coordinates[1] - 1))
            return spirit, next_coordinates
    if (spirit.orientacion == "sur"):
        if coordinates[1] + 1 < n and not ("Inferior" in lista):
            next_coordinates.append((coordinates[0], coordinates[1] + 1))

            return spirit, next_coordinates
        elif coordinates[0] - 1 >= 0 and not ("Izquierdo" in lista):
            tiempo+=4
            spirit.nuevaOrientacion("oeste")
            visitados.append("giro")
            next_coordinates.append((coordinates[0] - 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] - 1 >= 0 and not ("Superior" in lista):
            tiempo += 8
            spirit.nuevaOrientacion("norte")
            visitados.append("giro")
            visitados.append("giro")
            next_coordinates.append((coordinates[0], coordinates[1] - 1))
            return spirit,next_coordinates

        elif coordinates[0] + 1 < m and not ("Derecho" in lista):
            tiempo+=12
            spirit.nuevaOrientacion("este")
            visitados.append("giro")
            visitados.append("giro")
            visitados.append("giro")
            next_coordinates.append((coordinates[0] + 1, coordinates[1]))
            return spirit, next_coordinates
    if (spirit.orientacion == "oeste"):
        if coordinates[0] - 1 >= 0 and not ("Izquierdo" in lista):

            next_coordinates.append((coordinates[0] - 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] - 1 >= 0 and not ("Superior" in lista):
            tiempo+=4
            spirit.nuevaOrientacion("norte")
            visitados.append("giro")
            next_coordinates.append((coordinates[0], coordinates[1] - 1))
            return spirit, next_coordinates
        elif coordinates[0] + 1 < m and not ("Derecho" in lista):
            tiempo+=8
            spirit.nuevaOrientacion("este")
            visitados.append("giro")
            visitados.append("giro")

            next_coordinates.append((coordinates[0] + 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] + 1 < n and not ("Inferior" in lista):
            tiempo+=12
            spirit.nuevaOrientacion("sur")
            visitados.append("giro")
            visitados.append("giro")
            visitados.append("giro")

            next_coordinates.append((coordinates[0], coordinates[1] + 1))
            return spirit, next_coordinates
    if (spirit.orientacion == "norte"):
        if coordinates[1] - 1 >= 0 and not ("Superior" in lista):
            next_coordinates.append((coordinates[0], coordinates[1] - 1))
            return spirit, next_coordinates
        elif coordinates[0] + 1 < m and not ("Derecho" in lista):
            tiempo+=4
            spirit.nuevaOrientacion("este")
            visitados.append("giro")

            next_coordinates.append((coordinates[0] + 1, coordinates[1]))
            return spirit, next_coordinates
        elif coordinates[1] + 1 < n and not ("Inferior" in lista):
            tiempo+=8
            spirit.nuevaOrientacion("sur")
            visitados.append("giro")
            visitados.append("giro")

            next_coordinates.append((coordinates[0], coordinates[1] + 1))
            return spirit, next_coordinates
        elif coordinates[0] - 1 >= 0 and not ("Izquierdo" in lista):
            tiempo+=12
            spirit.nuevaOrientacion("oeste")
            visitados.append("giro")
            visitados.append("giro")
            visitados.append("giro")

            next_coordinates.append((coordinates[0] - 1, coordinates[1]))
            return spirit, next_coordinates


def dfs(maze, stack, spirit, visitados):
    start = spirit
    stack.append((start.coordenadaI,start.coordenadaJ))
    global contadorOrigen
    while stack:
        if(contadorOrigen==10):
            raise TypeError

        print("\n")
        n = stack.pop()
        if(n[0]==0 and n[0]==0):
            contadorOrigen += 1
        visitados.append(n)
        print(start.orientacion)
        print(f"Buscando en {n}")
        print(f"Es {n} mi objetivo?")
        print(n)
        if maze.getTerreno(n[0],n[1]).objetivo:
            print("Listo!")
            return
        print(f"No.")
        start,next_steps = find_next(start,n, maze, visitados)
        print(f"Siguiente: {next_steps}")
        stack.append(next_steps[0])


def main():
    spirit=Spirit("este",0,0)
    global m
    global n
    m=3
    n=3
    laberinto=Matriz(m,n)
    laberinto.generarArea()
    visitados=[]
    stack = []

    Tablero_game = Tablero(spirit,laberinto)
    Tablero_game.exportarTableroExcel()
    print("\n")
    
    try:
        dfs(laberinto, stack, spirit, visitados)
        print(f"Al Spirit le tomó un total de {tiempo}s encontrar el objetivo")
    except TypeError:
        print(f"Al Spirit le tomó un total de {tiempo}s darse cuenta que no hay solución")



    print(visitados)
if __name__ == "__main__":
    main()