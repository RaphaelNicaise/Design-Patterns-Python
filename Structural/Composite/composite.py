from abc import ABC, abstractmethod

class Componente(ABC):
    @abstractmethod
    def operacion(self):
        pass

class Hoja(Componente):
    def operacion(self):
        print("Realizando operacion en Hoja")

class Compuesto(Componente):
    def __init__(self):
        self._elementos = list()

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)

    def quitar_elemento(self, elemento):
        self._elementos.remove(elemento)

    def operacion(self):
        print("Realizando operacion en Composicion")
        i = 0
        for elemento in self._elementos:
            i += 1
            print(f"{i} - ", end="")
            elemento.operacion()

hoja1 = Hoja()
hoja2 = Hoja()

comp1 = Compuesto()

comp1.agregar_elemento(hoja1)
comp1.agregar_elemento(hoja2)

comp1.operacion()

hoja3 = Hoja()

comp2 = Compuesto()
comp2.agregar_elemento(comp1)
comp2.agregar_elemento(hoja3)

comp2.operacion()