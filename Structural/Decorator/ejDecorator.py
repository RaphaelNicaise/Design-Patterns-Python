from abc import ABC, abstractmethod

class Auto(ABC):
    @abstractmethod
    def precio(self)->float:
        pass

    @abstractmethod
    def caracteristicas(self)->dict:
        pass

class AutoConcreto(Auto):
    def __init__(self, nombre, precio_base):
        self._nombre = nombre
        self._precio = precio_base

    def precio(self):
        return self._precio
    
    def caracteristicas(self):
        return dict(
            nombre = self._nombre,
            precio = self._precio,
            accesorios = list()
        )
    
class Decorator(Auto):
    def __init__(self, auto: Auto):
        self._auto = auto

class DecoratorAireAcondicionado(Decorator): # Cada decorador le agrega funcionalidad o caracteristicas nuevas al objeto base (Auto)
    def __init__(self, auto: Auto):
        super().__init__(auto)

    def precio(self):
        return self._auto.precio() + 2000 # costo adicional por tener aire
    
    def caracteristicas(self):
        caracteristicas = self._auto.caracteristicas()
        if not "Aire Acondicionado" in caracteristicas["accesorios"]:
            caracteristicas["precio"] = self.precio()
            caracteristicas["accesorios"].append("Aire Acondicionado")
        return caracteristicas

class DecoratorSistemaBluetooth(Decorator):
    def __init__(self, auto: Auto):
        super().__init__(auto)

    def precio(self):
        return self._auto.precio() + 1500
    
    def caracteristicas(self):
        caracteristicas = self._auto.caracteristicas()
        if not "Bluetooth" in caracteristicas["accesorios"]:
            caracteristicas["precio"] = self.precio()
            caracteristicas["accesorios"].append("Bluetooth")
        return caracteristicas

auto_base = AutoConcreto("Peugeot 208", 15000)
print(auto_base.caracteristicas()) # -> {'nombre': 'Peugeot 208', 'precio': 15000, 'accesorios': []}

auto_con_aire = DecoratorAireAcondicionado(auto_base)
print(auto_con_aire.caracteristicas()) # -> {'nombre': 'Peugeot 208', 'precio': 17000, 'accesorios': ['Aire Acondicionado']}

auto_con_aire_y_bluetooth = DecoratorSistemaBluetooth(auto_con_aire)
print(auto_con_aire_y_bluetooth.caracteristicas()) # -> {'nombre': 'Peugeot 208', 'precio': 18500, 'accesorios': ['Aire Acondicionado', 'Bluetooth']}