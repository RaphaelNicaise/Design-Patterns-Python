import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self) 
    
class ConcretePrototype(Prototype):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f"{self.name}: {self.value}"
    
# creamos prototipo, clase que nos va a ayudar a crear clases despues
prototype = ConcretePrototype("prot", 1)
print(prototype) # -> prot: 1

clone = prototype.clone() # creamos objeto clon en base al prototipo
print(clone) # -> prot: 1

# modificamos al clone
clone.value = 2

# verificamos que sean distinto
print("\nVerificacion:")
print(f"Prototype -> {prototype}")
print(f"Clone -> {clone}")
