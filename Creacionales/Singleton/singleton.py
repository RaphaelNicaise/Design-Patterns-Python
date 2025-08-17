class Singleton:
    __instance = None 
 
    def __init__(self):
        if Singleton.__instance != None:
            raise SingletonException
        else: 
            Singleton.__instance = self 

    @staticmethod
    def getInstance():
        # esta funcion permite obtener la instancia unica de la clase

        if Singleton.__instance == None:
            Singleton() # construimos el objeto si no existe la instancia
        return Singleton.__instance # retornamos la instance (None si no se instancio)
        
class SingletonException(Exception):
    msg = "La clase ya a sido instanciada"
    def __init__(self, msg):
        super().__init__(msg)

if __name__ == "__main__":
    singleton1 = Singleton.getInstance()
    singleton2 = Singleton.getInstance() 

    # devuelve el unico objeto creado en la primera instanciacion dentro de getInstance