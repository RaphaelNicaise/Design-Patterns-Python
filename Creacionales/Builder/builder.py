class Product: # clase que vamos a construir
    def __init__(self): # sin parametros
        self.part_a = ""
        self.part_b = ""
        self.part_c = ""

class Builder:
    # define la interfaz para constuir paso a paso

    def __init__(self):
        self._product = Product()

    # setters del producto
    def set_part_a(self):
        self._product.part_a = "A"

    def set_part_b(self):
        self._product.part_b = "B"

    def set_part_c(self):
        self._product.part_c = "C"

    def get_product(self):
        product = self._product
        return product


class Director:
    #Se construyen distintos productos mediante el builder
    
    def __init__(self, builder: 'Builder'):
        self._builder = builder

    def build_pr1(self):
        self._builder.set_part_a()

    def build_pr2(self):
        self._builder.set_part_a()
        self._builder.set_part_b()
        self._builder.set_part_c()


if __name__ == "__main__":
    builder = Builder()
    director = Director(builder)

    director.build_pr1()
    product1 = builder.get_product()
    print("pr1:", product1.__dict__)

    director.build_pr2()
    product2 = builder.get_product()
    print("pr2:", product2.__dict__)
