# define los metodos para crear objetos relacionados entre si sin especificar su clase concreta
class AbstractFactory:
    def crear_producto_a(self):
        pass

    def crear_producto_b(self):
        pass

# definicion clase concreta Factory
class Factory1(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA1()

    def crear_producto_b(self):
        return ProductoB1()
    
class Factory2(AbstractFactory):
    def crear_producto_a(self):
        return ProductoA2()

    def crear_producto_b(self):
        return ProductoB2()
    
class ProductoA:
    def descripcion(self):
        pass

class ProductoA1(ProductoA):
    def descripcion(self):
        return "Soy un producto de tipo A1"
    
class ProductoA2(ProductoA):
    def descripcion(self):
        return "Soy un producto de tipo A2"
    
class ProductoB:
    def descripcion(self):
        pass

class ProductoB1(ProductoB):
    def descripcion(self):
        return "Soy un producto de tipo B1"
    
class ProductoB2(ProductoB):
    def descripcion(self):
        return "Soy un producto de tipo B2"
    

if __name__ == "__main__":
    factory_1 = Factory1()

    producto_a1 = factory_1.crear_producto_a() # como es factory1 ya sabemos que el A va a ser A1
    producto_b1 = factory_1.crear_producto_b()

    print(producto_a1.descripcion())
    print(producto_b1.descripcion())

    factory_2 = Factory2()
    producto_a2 = factory_2.crear_producto_a()
    producto_b2 = factory_2.crear_producto_b()
    
    print(producto_a2.descripcion())
    print(producto_b2.descripcion())