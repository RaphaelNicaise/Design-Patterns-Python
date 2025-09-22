# 2. Cartas de un juego

# Estado compartido: Número, palo, imagen de la carta
# Estado único: Posición en la mesa, si está boca arriba/abajo, a qué jugador pertenece
# Escenario: Múltiples barajas, muchas cartas iguales

# Flyweight
class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"
    
class Card:
    SUITS = ["♥️", "♦️", "♣️", "♠️"]
    VALUES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self, suit, value):
        self.suit = suit if suit in self.SUITS else None          # shared_state
        self.value = value if str(value) in self.VALUES else None # shared_state
    
    def show_card(self,state:str, player: Player=None): 
        return f"{self.value}{self.suit}  State: {state} Player: {player if player else None} ID_CARD: {id(self)}"


class CardFactory:
    def __init__(self):
        self.cards = {}

    def get_card(self, suit, value)->Card:
        key = (suit, value)
        if key not in self.cards:
            self.cards[key] = Card(suit, value) # si la carta no existe, la crea
        return self.cards[key] # si ya existe, devuelve la que ya está en memoria
    
if __name__ == "__main__":
    card = Card('♥️', 'A')
    print(card.show_card("on table", Player("Rapha")))
    card2 = Card('♥️', 'A')
    print(card2.show_card("in hand", Player("Pepe"))) 
    # dos objetos distintos en memoria porque usamos la factory

    factory = CardFactory()
    card3 = factory.get_card('♣️','K')  
    print(card3.show_card('played',Player("Rapha")))
    card4 = factory.get_card('♣️','K')
    print(card4.show_card('in deck',Player("Pepe")))
    # ambos apuntan al mismo objeto en memoria
