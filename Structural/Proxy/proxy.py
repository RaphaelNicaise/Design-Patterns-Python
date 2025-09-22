# Proxy se encarga de realizar operaciones posteriores a la invocacion de metodos
# se utiliza para validaciones, logging, control de acceso
#  Proxy y Decorator son muy parecidos conceptualmente - ambos "envuelven" un objeto para agregar funcionalidad
class ServiceInterface:
    def accion(self):
        pass

class Service:
    def accion(self):
        print("Servicio: Ejecutando la accion")

class Proxy(ServiceInterface):
    def __init__(self):
        self.service = None

    def accion(self):
        if self.service is None:
            self.service = Service() # Inicializamos el servicio
        print("Proxy: Realizando operaciones antes de la llamada al servicio")
        self.service.accion() # Delegamos la llamada al servicio

if __name__ == "__main__":
    proxy = Proxy()
    proxy.accion()