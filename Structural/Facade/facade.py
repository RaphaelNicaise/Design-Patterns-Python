class Subsistema1:
    def operacion1(self):
        print("Operacion 1 en Subsistema 1")

class Subsistema2:
    def operacion2(self):
        print("Operacion 2 en Subsistema 2")

class Subsistema3:
    def operacion3(self):
        print("Operacion 3 en Subsistema 3")

class Facade: # interfaz para interactuar con los subsistemas de forma sencilla
    def __init__(self): 
        # enlaces a objetos de los subsistemas
        self._subsistema1 = Subsistema1()
        self._subsistema2 = Subsistema2()
        self._subsistema3 = Subsistema3()

    def operacion_compleja(self):
        print("Iniciando Operacion Compleja")
        self._subsistema1.operacion1()
        self._subsistema2.operacion2()
        self._subsistema3.operacion3()

Facade().operacion_compleja()
