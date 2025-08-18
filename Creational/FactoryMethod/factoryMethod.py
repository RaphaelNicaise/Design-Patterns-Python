# clase abstracta Producto
class Producto:
    def descripcion(self):
        pass

# definicion de clase concreta ProductoA y B que implementan la interfaz Producto
class ProductoA(Producto):
    def descripcion(self):
        return "Este es el ProductoA"
    
class ProductoB(Producto):
    def descripcion(self):
        return "Este es el ProductoB"
    
# clase abstracta Creador
class Creador:
    def crearProducto(self):
        pass

class CreadorA(Creador):
    def crearProducto(self):
        return ProductoA()
    
class CreadorB(Creador):
    def crearProducto(self):
        return ProductoB()
    
if __name__ == "__main__":
    creador_a = CreadorA()
    producto_a = creador_a.crearProducto()
    print(producto_a.descripcion()) # Producto A

    creador_b = CreadorB()
    producto_b = creador_b.crearProducto()
    print(producto_b.descripcion())