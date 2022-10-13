from modified_hash import *

NO_HAY_ARISTA = -1

class Grafo:
	def __init__(self, nombre_vertices, dirigido):
		self.vertices = Dict_()
		self.dirigido = dirigido
		for nombre in nombre_vertices:
			self.insertar_vertice(nombre)

	def obtener_vertices(self):
		return self.vertices.keys()

	def insertar_vertice(self, nombre_vertice):
		if not self.existe_vertice(nombre_vertice):
			self.vertices.insert(Dict_(), nombre_vertice)

	def insertar_arista(self, origen, destino, peso = 1):
		self.vertices.access(origen).insert(peso, destino)

	def eliminar_vertice(self, vertice):
		if self.existe_vertice(vertice):
			if not self.dirigido:
				for adyacente in self.adyacentes(vertice):
					self.vertices.access(adyacente).remove(vertice)
			self.vertices.remove(vertice)

	def adyacentes(self, vertice):
		return self.vertices.access(vertice).keys()

	def cantidad_de_adyacentes(self, vertice):
		return self.vertices.access(vertice).size()

	def existe_vertice(self, vertice):
		return self.vertices.includes(vertice)

	def existe_arista(self, inicio, fin):
		if not (self.existe_vertice(inicio)):
			return False
		return self.vertices.access(inicio).includes(fin)

	def arista_peso(self, inicio, fin):
		if self.existe_arista(inicio, fin):
			return self.vertices.access(inicio).access(fin)
		return NO_HAY_ARISTA

	def imprimir(self):
		for vertice in self.vertices.keys():
			string = f'{vertice}'
			for adyacente in self.adyacentes(vertice):
				string += f',{adyacente}'
			print(string)
