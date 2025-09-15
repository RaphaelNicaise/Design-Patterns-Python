# sistema de archivos
from abc import ABC, abstractmethod

# los archivos y carpetas son tratados como elementos aunque a veces uno este compuesto de varios de otro 
# elemento (carpeta) / elemento (archivo)
#                    / elemento (archivo)
#                    / elemento (archivo)

class Elemento(ABC): 
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def abrir(self):
        pass

class Archivo(Elemento):
    
    def __init__(self,nombre_archivo:str ,contenido = None):
        super().__init__(nombre_archivo)
        self._contenido = contenido 
    
    def abrir(self)->str:
        print(f"Contenido de {self._nombre}  -> {self._contenido}")

    
class Carpeta(Elemento):
    def __init__(self, nombre_carpeta):
        super().__init__(nombre_carpeta)
        self._elementos = list() # se crea carpeta sin ningun elemento
    
    def abrir(self)->str:
        print(f"Abriendo carpeta {self.nombre}...")    
        for elemento in self._elementos:
            elemento.abrir()

    def agregar_elemento(self, elemento):
        self._elementos.append(elemento)
    
    def quitar_elemento(self, elemento):
        self._elementos.remove(elemento)

archivo_1 = Archivo("documento.pdf", "Hola 123")
# archivo_1.abrir() # contenido de archivo

carpeta_pdfs = Carpeta("PDFs")
carpeta_pdfs.agregar_elemento(archivo_1)
carpeta_pdfs.abrir()

carpeta_home = Carpeta("Home")
carpeta_home.agregar_elemento(carpeta_pdfs) # home/pdfs/documento.pdf

carpeta_home.abrir()


