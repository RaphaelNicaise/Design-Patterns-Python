from abc import ABC, abstractmethod

class InterfaceDispositivos(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

class ImplementacionTelevisor(InterfaceDispositivos):
    def encender(self):
        print("Encendiendo Televisor")

    def apagar(self):
        print("Apagando Televisor")

    def cambiar_canal(self):
        print("Cambiando Canal")

class ImplementacionAire(InterfaceDispositivos):
    def encender(self):
        print("Encendiendo Aire Acondicionado")

    def apagar(self):
        print("Apagando Aire Acondicionado")

    def cambiar_temperatura(self):
        print("Cambiando Temperatura")

class ImplementacionRadio(InterfaceDispositivos):
    def encender(self):
        print("Encendiendo Radio")

    def apagar(self):
        print("Apagando Radio")

    def cambiar_frecuencia(self):
        print("Cambiando Frecuencia")

class AbstraccionControlRemoto:
    
    def __init__(self, interface_instance: InterfaceDispositivos):
        """
            Se instancia dentro de la abstraccion
        Args:
            interface_instance (InterfaceDispositivos)
        """
       
        # verificacion si es clase o instancia
        if isinstance(interface_instance, type):
            self._interface = interface_instance()  # instanciar si es clase
        else:
            self._interface = interface_instance    # usar directamente si es instancia

    def funcionalidad_encender(self):
        self._interface.encender()

    def funcionalidad_apagar(self):
        self._interface.apagar()

    def funcionalidad_cambiar(self):
        match self._interface:
            case d if isinstance(d, ImplementacionTelevisor):
                self._interface.cambiar_canal()
            case d if isinstance(d, ImplementacionAire):
                self._interface.cambiar_temperatura()
            case d if isinstance(d, ImplementacionRadio):
                self._interface.cambiar_frecuencia()

abstraccion_control_televisor = AbstraccionControlRemoto(ImplementacionTelevisor)
abstraccion_control_televisor.funcionalidad_encender()

abstraccion_control_televisor.funcionalidad_cambiar()


abstraccion_control_aire = AbstraccionControlRemoto(ImplementacionAire)

abstraccion_control_aire.funcionalidad_encender()
abstraccion_control_aire.funcionalidad_cambiar()