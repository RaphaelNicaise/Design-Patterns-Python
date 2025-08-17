import copy

class PrototypePlayer:
    def clone(self):
        return copy.deepcopy(self)
    
class Player(PrototypePlayer):
    def __init__(self, name: str= "Joe Doe", age: int= 0):
        self.__name = name 
        self.__age = age
        self.__attributes = dict(
            health = 0,
            strenght = 0,
            agility = 0,
            intelligence = 0
        )

    def __repr__(self):
        return f'Player("{self.name}",{self.age},"{self.attributes}")'
    
    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    
    @property
    def attributes(self):
        return self.__attributes

    @name.setter
    def name(self, name):
        if not (isinstance(name, str) and (0 < len(name) <= 100)):
            return False
         
        self.__name = name

    @age.setter
    def age(self, age):
        if not (isinstance(age, int) and (0 < age <=100)):
            return False
        self.__age = age

    def setAttribute(self, attribute, value):
        if not between0and100(value):
            print("El valor no es correcto")
            return False
                
        self.attributes[attribute] = value
    
    def setHealth(self, value):
        self.setAttribute('health', value)

    def setStrenght(self, value):
        self.setAttribute('strenght', value)

    def setAgility(self, value):
        self.setAttribute('agility', value)

    def setIntelligence(self, value):
        self.setAttribute('intelligence', value)


def between0and100(value): return isinstance(value, int) and (0 <= value <= 100)  

if __name__ == "__main__":
    prototype = Player() # creamos el prototype de player con sus datos default
    print(f"Prototype -> {prototype}\n") # -> Player("Joe Doe",0,"{'health': 0, 'strenght': 0, 'agility': 0, 'intelligence': 0}")

    player1 = prototype.clone() # creamos un player en base a la instancia del clone
    print(f"Clone -> {player1}\n") # -> Player("Joe Doe",0,"{'health': 0, 'strenght': 0, 'agility': 0, 'intelligence': 0}")

    # modificamos el clone
    player1.name = "Rapha"
    player1.age = 53
    player1.setHealth(40)
    player1.setAgility(30)
    player1.setStrenght(50)
    player1.setIntelligence(43)
    print(f"Clone Modificado -> {player1}") # -> Player("Rapha",0,"{'health': 40, 'strenght': 50, 'agility': 30, 'intelligence': 43}")