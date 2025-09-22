class Expresion:
    def interpretar(self):
        pass
    
class Numero(Expresion): # expresion simple
    def __init__(self, value):
        self.value = value

    def interpretar(self):
        return self.value
    
class Sumar(Expresion): # expresion compuesta de expresiones simples
    def __init__(self, izq:Expresion, der:Expresion):
        self.izq = izq if isinstance(izq, Expresion) else Numero(izq)
        self.der = der if isinstance(der, Expresion) else Numero(der)
    
    def interpretar(self):
        return self.izq.interpretar() + self.der.interpretar()
    
class Restar(Expresion):
    def __init__(self, izq:Expresion, der:Expresion):
        self.izq = izq if isinstance(izq, Expresion) else Numero(izq)
        self.der = der if isinstance(der, Expresion) else Numero(der)

    def interpretar(self):
        return self.izq.interpretar() - self.der.interpretar()
    
class Multiplicar(Expresion):
    def __init__(self, izq:Expresion, der:Expresion):
        self.izq = izq if isinstance(izq, Expresion) else Numero(izq)
        self.der = der if isinstance(der, Expresion) else Numero(der)
    
    def interpretar(self):
        return self.izq.interpretar() * self.der.interpretar()
    
class Elevar(Expresion):
    def __init__(self, base:Expresion, exponente:Expresion):
        self.base = base if isinstance(base, Expresion) else Numero(base)
        self.exponente = exponente if isinstance(exponente, Expresion) else Numero(exponente)

    def interpretar(self):
        return self.base.interpretar() ** self.exponente.interpretar()

class Dividir(Expresion):
    def __init__(self, izq:Expresion, der:Expresion):
        self.izq = izq if isinstance(izq, Expresion) else Numero(izq)
        self.der = der if isinstance(der, Expresion) else Numero(der)

    def interpretar(self):
        try:
            return self.izq.interpretar()/self.der.interpretar()
        except ZeroDivisionError as e:
            print("No se puede dividir por 0")

class Raiz(Expresion):
    def __init__(self, izq:Expresion, der: Expresion):
        self.izq = izq if isinstance(izq, Expresion) else Numero(izq)
        self.der = der if isinstance(der, Expresion) else Numero(der)

    def interpretar(self):
        return Elevar(self.izq, Dividir(Numero(1),self.der)).interpretar()

if __name__ == "__main__":
    # 1 + 3 * 4**2
    calculo1 = Sumar(Numero(1),Multiplicar(Numero(3),(Elevar(Numero(4),Numero(2))))).interpretar()
    print(calculo1)
    # implemente que se pueda hacer
    # asi ahora ya que se instancian los numeros dentro de las expresiones complejas
    calculo2 = Sumar(1,Multiplicar(3,(Elevar(4,2)))).interpretar()
    print(calculo2)