class Terreno:

    def __init__(self,tipo,obstaculo):
        self.tipo = tipo
        self.obstaculo = obstaculo
        self.objetivo = False
    
    def getTipoTerreno(self):
        return self.tipo

    def getObstaculosTerreno(self):
        return self.obstaculo

    def getDetalleTerreno(self):
        return ("Terreno Llano") if self.tipo == 0 else ("Terreno Abrupto")

    def getDetalleObstaculo(self):
        detalle = ""
        hayObstaculos = False
        for i in range(4):
            if self.obstaculo[i] == 1 and i == 0:
                detalle+= "Obstaculo Superior"
                detalle+= "; "
                hayObstaculos = True
            elif self.obstaculo[i] == 1 and i == 1:
                detalle+= "Obstaculo Costado Derecho"
                detalle+= "; "
                hayObstaculos = True
            elif self.obstaculo[i] == 1 and i == 2:
                detalle+= "Obstaculo Inferior"
                detalle+= "; "
                hayObstaculos = True
            elif self.obstaculo[i] == 1 and i == 3:
                detalle+= "Obstaculo Costado Izquierdo"
                hayObstaculos = True
        return detalle if hayObstaculos else "No hay Obstaculos" 

    def asignarTerrenoObjetivo(self):
        self.objetivo = True

    def esObjetivo(self):
        return self.objetivo