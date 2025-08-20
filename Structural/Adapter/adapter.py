from abc import ABC, abstractmethod

# Interfaz que define como se interactua con el servicio
class Interface(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    @abstractmethod
    def method2(self):
        pass

# Clase util q se quiere usar en otra parte del programa, pero no se puede usar porque tiene una interfaz incompatible
class Service:
    def method1(self):
        return "Method 1"

# es capaz de comunicar al cliente con el servicio
# basicamente el cliente manda una solicitud al adapter, y el adapter la convierte en algo 
# q el service pueda entender, utilizando el servicio para realizar la tarea
class ServiceAdapter(Interface):
    def __init__(self, service):
        self.service = service

    def method1(self):
        return self.service.method1()
    
    def method2(self):
        return "Method 2 adapted"
    
service = Service()

adapter = ServiceAdapter(service)

print(adapter.method1())
print(adapter.method2())