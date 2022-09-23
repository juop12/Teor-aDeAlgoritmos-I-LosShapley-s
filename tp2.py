from csv import reader
#import pudb; pu.db

class Caja:
	def __init__(self, identificacion, largo, alto):
		self.largo = largo
		self.alto = alto
		self.id = identificacion

class Repisa:
	def __init__(self, largo):
		self.largo = largo
		self.cajas = []
		self.espacioDisponible = largo
		self.alturaMax = 0

	def tiene_espacio(self ,espacioAConsultar):
		return (self.espacioDisponible - espacioAConsultar) >= 0

	def insertar_caja(self, caja):
		if self.tiene_espacio(caja.largo):
			self.cajas.append(caja)
			self.alturaMax = max(self.alturaMax, caja.alto) 
			self.espacioDisponible = self.espacioDisponible - caja.largo
			return True
		return False

class Optimo:
	def__init__(self, repisa, optimo_previo):
		self.repisa = repisa
		self.optimo_previo = optimo_previo
		
def levantar_cajas_csv(cajas, nombreDeArchivo):
    with open(nombreDeArchivo) as archivo:
        for linea in reader(archivo): #n; n = cantidad de lineas (cantidad de socios)
        	cajas.append(Caja(int(linea[0]), int(linea[1]), int(linea[2])))
           
    return cajas


def ordenadar_almacen(cantidadCajas, largoRepisas, nombreDeArchivo):
	cajas = []
	cajas.append(Caja(0,0,0))
	cajas = levantar_cajas_csv(cajas ,nombreDeArchivo)
	optimos = []
	alturasMaximas = {}
	for i in range(cantidadCajas + 1):
		optimos.append(-1) 
	optimos[0] = 0
	return opt(cajas ,cajas[cantidadCajas], alturasMaximas, optimos, largoRepisas)


def altura_maxima(matrizComparacion, cajas, inicio, fin):
	if inicio in matrizComparacion.keys():
		if fin in matrizComparacion[inicio].keys():
			return matrizComparacion[inicio][fin]
		matrizComparacion[inicio][fin] = max(cajas[fin].alto, altura_maxima(matrizComparacion, cajas, inicio, fin-1))
		return matrizComparacion[inicio][fin]

	matrizComparacion[inicio] = {} 
	matrizComparacion[inicio][inicio] = cajas[inicio].alto

	return altura_maxima(matrizComparacion, cajas, inicio, fin)


def opt(cajas, cajaActual, alturasMaximas, optimos, largoRepisas):
	
	if optimos[cajaActual.id] != -1:
		print('puta')
		return optimos[cajaActual.id]

	mejor_optimo = -1
	nuevaRepisa = Repisa(largoRepisas)
	i = 0

	print(cajas[cajaActual.id].id)

	while ((cajaActual.id - i) > 0) and nuevaRepisa.insertar_caja(cajas[cajaActual.id - i]):
		print('entro')
		i+= 1
		optimo_calculado = opt(cajas, cajas[cajaActual.id - i], alturasMaximas, optimos, largoRepisas) + altura_maxima(alturasMaximas ,cajas ,cajaActual.id - i + 1,cajaActual.id)
		if (mejor_optimo == -1) or (mejor_optimo > optimo_calculado):
			mejor_optimo = optimo_calculado

	optimos[cajaActual.id] = mejor_optimo
	print(optimos)
	return mejor_optimo

def main():
	print('a')
	print(ordenadar_almacen(6, 3, "/home/pal/Desktop/tda/tpw/ejemplo/ejemplo3.csv"))

main()

