# basicamente agarrar objetos que ya existen en memoria en vez de crear nuevos
# y asi ahorrar memoria

class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Flyweight con estado compartido {self.shared_state} y estado unico {unique_state}")

class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, shared_state):
        if shared_state not in self.flyweights:
            self.flyweights[shared_state] = Flyweight(shared_state)
        return self.flyweights[shared_state]
    
factory = FlyweightFactory()
print(factory)

fly1 = factory.get_flyweight('AAA123')
fly1.operation('ESTADO UNICO AAA1')

fly2 = factory.get_flyweight('AAA123')
fly2.operation('ESTADO UNICO BBB2')

fly3 = factory.get_flyweight('AAA123')
fly3.operation('ESTADO UNICO CCC3')
# los tres apuntan al MISMO objeto en memoria. La factory solo crea un nuevo Flyweight si no existe uno con ese estado compartido.
print(factory.get_flyweight('AAA123'))