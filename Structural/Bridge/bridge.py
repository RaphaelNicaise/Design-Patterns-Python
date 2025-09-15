from abc import ABC, abstractmethod

class Interface(ABC):
    @abstractmethod
    def method(self):
        pass

class ImplementacionConcreta1(Interface):
    def method(self):
        print("Implementacion concreta 1")

class ImplementacionConcreta2(Interface):
    def method(self):
        print("Implementacion concreta 2")

class Abstraccion:
    def __init__(self, interface: Interface):
        self.interface = interface

    def funcionalidad(self):
        self.interface.method() # ejecuta el metodo de la interface q le pasemos

abstraccion1 = Abstraccion(ImplementacionConcreta1()) # hay que pasarle una instancia de la interfaz
abstraccion1.funcionalidad() # lo que va a ejecutar es el metodo de la interface

abstraccion2 = Abstraccion(ImplementacionConcreta2())
abstraccion2.funcionalidad()