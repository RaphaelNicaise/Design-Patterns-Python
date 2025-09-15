from abc import ABC, abstractmethod

class Componente(ABC):
    def operacion(self):
        pass

class ComponenteConcreto(Componente):
    def operacion(self):
        print("Realizando operacion en Componente Concreto")

class Decorator(Componente):
    def __init__(self, componente: Componente):
        self._componente = componente

    def operacion(self):
        self._componente.operacion()

class DecoratorConcreto(Decorator):
    def __init__(self, componente: Componente):
        super().__init__(componente)

    def funcion_agregada(self):
        print("Agregando funcionalidad al componente")
        
    def operacion(self):
        super().operacion()
        self.funcion_agregada()

componente = ComponenteConcreto()
print("Operacion de Componente sin decorador: ")
componente.operacion()

decorador = DecoratorConcreto(componente)
print("\nOperacion de Componente con decorador:")
decorador.operacion()