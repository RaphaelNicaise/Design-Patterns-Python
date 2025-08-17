# pizza <- pizzabuilder <- director

class Pizza:
    
    def __init__(self): # no colocamos parametros ya que los atributos los construiremos
        self.size = ""
        self.cheese = False
        self.pepperoni = False
        self.ham = False
        self.mushrooms = False
        self.tomatoes = False
        self.masa_type = ""
      
class PizzaBuilder:
    # Clase builder que define los metodos para construir los objetos
    __instance = None # le voy a agregar singleton para practicar

    sizes = ['s','m','l','xl']
    masa_types = ['new-york','sicilian','thin-crust','napolitean']

    def __init__(self):
        
        if PizzaBuilder.__instance != None:
            raise Exception('Ya hay una instancia del Builder')
        else:
            PizzaBuilder.__instance = self

        self.pizza = Pizza()

    @staticmethod
    def getInstance():
        """Obtener instancia del Builder"""
        if PizzaBuilder.__instance == None:
            PizzaBuilder()
        return PizzaBuilder.__instance


    def setSize(self, size):
        if size in PizzaBuilder.sizes:
            self.pizza.size = size

    def addCheese(self): self.pizza.cheese = True

    def addPepperoni(self): self.pizza.pepperoni = True

    def addHam(self): self.pizza.ham = True

    def addMushrooms(self): self.pizza.mushrooms = True

    def addTomatoes(self): self.pizza.tomatoes = True

    def setMasaType(self, masa_type):
        if masa_type in PizzaBuilder.masa_types:
            self.pizza.masa_type = masa_type

    def getPizza(self):
        return self.pizza
        
class Director:
    # El director se encarga de construir distintos tipos de pizza mediante el builder
    def __init__(self, builder):
        self._builder:'PizzaBuilder' = builder

    def construct_margarita(self):
        self._builder.setSize('m')
        self._builder.addCheese()
        self._builder.addTomatoes()
        self._builder.setMasaType('thin-crust')

    def construct_pepperoni(self):
        self._builder.setSize('l')
        self._builder.addCheese()
        self._builder.addPepperoni()
        self._builder.addMushrooms()
        self._builder.setMasaType('new-york')

if __name__ == "__main__":
    builder = PizzaBuilder.getInstance() # instanciamos pizza builder
    
    director = Director(builder) # creamos el director encargado de crear las pizzas

    director.construct_margarita() # se construye la pizza
    pizza1 = builder.getPizza()
    print(pizza1.__dict__)

    director.construct_pepperoni()
    pizza2 = builder.getPizza()
    print(pizza2.__dict__)
    
