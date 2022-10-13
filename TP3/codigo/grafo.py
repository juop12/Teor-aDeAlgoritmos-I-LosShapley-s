NO_HAY_ARISTA = -1

class Grafo:
	def __init__(self, nombre_vertices, dirigido):
		self.vertices = {}
		self.dirigido = dirigido
		for nombre in nombre_vertices:
			self.vertices[nombre] = {}

	def obtener_vertices(self):
		return self.vertices.keys()

	def insertar_vertice(self, nombre_vertice):
		if not self.existe_vertice(nombre_vertice):
			self.vertices[nombre_vertice] = {}

	def insertar_arista(self, origen, destino, peso = 1):
		self.vertices[origen][destino] = peso
		if not self.dirigido:
			self.vertices[destino][origen] = peso

	def eliminar_vertice(self, vertice):
		if self.existe_vertice(vertice):
			if not self.dirigido:
				for adyacente in self.adyacentes(vertice):
					del self.vertices[adyacente][vertice]
			del self.vertices[vertice]

	def adyacentes(self, vertice):
		return self.vertices[vertice].keys()

	def cantidad_de_adyacentes(self, vertice):
		return len(self.vertices[vertice])

	def existe_vertice(self, vertice):
		return vertice in self.vertices

	def existe_arista(self, inicio, fin):
		if not (self.existe_vertice(inicio)):
			return False
		return fin in self.vertices[inicio]

	def arista_peso(self, inicio, fin):
		if self.existe_arista(inicio, fin):
			return self.vertices[inicio][fin]
		return NO_HAY_ARISTA

	def imprimir(self):
		for vertice in self.vertices.keys():
			string = f'{vertice}'
			for adyacente in self.adyacentes(vertice):
				string += f',{adyacente}'
			print(string)
