class Nodo:
	def __init__(self, dato, siguiente=None):
		self.dato = dato
		self.siguiente = siguiente

class Cola:
	def __init__(self):
		self.inicio = None
		self.tope = None
		self.largo = 0

	def encolar(self, dato):
		nuevoNodo = Nodo(dato)
		self.largo += 1

		if self.esta_vacia():
			self.inicio = nuevoNodo
			self.tope = nuevoNodo
			return

		self.tope.siguiente = nuevoNodo
		self.tope = nuevoNodo

	def desencolar(self):
		if self.esta_vacia(): 
			return None

		dato = self.inicio.dato
		self.inicio = self.inicio.siguiente

		self.largo -= 1
		if self.len() == 0:
			self.tope = None
			
		return dato

	def frente(self):
		if self.esta_vacia():
			return None
		return self.inicio.dato

	def len(self):
		return self.largo

	def esta_vacia(self):
		return self.tope is None
