class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, dato):
        self.tope = Nodo(dato, self.tope)

    def desapilar(self):
        if self.esta_vacia(): 
            return None
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            return None
        return self.tope.dato

    def esta_vacia(self):
        return self.tope is None

class Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox