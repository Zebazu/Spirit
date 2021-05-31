from Matriz import Matriz
from Spirit import Spirit
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
    print("\n")
    try:
        dfs(laberinto, stack, spirit, visitados)
        print(f"Al Spirit le tomó un total de {tiempo}s encontrar el objetivo")
    except TypeError:
        print(f"Al Spirit le tomó un total de {tiempo}s darse cuenta que no hay solución")



    print(visitados)
if __name__ == "__main__":
    main()