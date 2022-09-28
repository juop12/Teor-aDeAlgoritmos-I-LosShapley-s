from csv import reader
from sys import argv
#import pudb; pu.db

class Caja:
	def __init__(self, identificacion, largo, alto):
		self.largo = largo
		self.alto = alto
		self.id = identificacion

	def __str__(self):
		if(self.largo == 0):
			return ''
		cadena = str(self.id) + ":(A" + str(self.alto) + " / L" + str(self.largo) + ")"
		return cadena

class Repisa:
	def __init__(self, largo):
		self.largo = largo
		self.espacioDisponible = largo

	def tiene_espacio(self ,espacioAConsultar):
		return (self.espacioDisponible - espacioAConsultar) >= 0

	def insertar_caja(self, caja):
		if self.tiene_espacio(caja.largo):
			self.espacioDisponible = self.espacioDisponible - caja.largo
			return True
		return False
		
def levantar_cajas_csv(cajas, nombreDeArchivo):
    with open(nombreDeArchivo) as archivo:
        for linea in reader(archivo): 
        	cajas.append(Caja(int(linea[0]), int(linea[1]), int(linea[2])))
           
    return cajas


def ordenadar_almacen(cantidadCajas, largoRepisas, cajas):
	
	optimos = []
	caminosOptimos = []
	alturasMaximas = {}

	for i in range(cantidadCajas + 1):
		optimos.append(-1) 
		caminosOptimos.append(0)
	optimos[0] = 0

	opt(cajas ,cajas[cantidadCajas].id, alturasMaximas, optimos, caminosOptimos, largoRepisas)

	return optimos, caminosOptimos, alturasMaximas


def altura_maxima(matrizComparacion, cajas, inicio, fin):
	if inicio in matrizComparacion.keys():
		if fin in matrizComparacion[inicio].keys():
			return matrizComparacion[inicio][fin]
		matrizComparacion[inicio][fin] = max(cajas[fin].alto, altura_maxima(matrizComparacion, cajas, inicio, fin-1))
		return matrizComparacion[inicio][fin]

	matrizComparacion[inicio] = {} 
	matrizComparacion[inicio][inicio] = cajas[inicio].alto

	return altura_maxima(matrizComparacion, cajas, inicio, fin)


def opt(cajas, idActual, alturasMaximas, optimos, caminosOptimos, largoRepisas):
	
	if optimos[idActual] != -1:
		return optimos[idActual]

	mejor_optimo = -1
	nuevaRepisa = Repisa(largoRepisas)
	i = 0

	while ((idActual - i) > 0) and nuevaRepisa.insertar_caja(cajas[idActual - i]):
		i+= 1
		optimo_calculado = opt(cajas, idActual - i, alturasMaximas, optimos, caminosOptimos, largoRepisas) + altura_maxima(alturasMaximas ,cajas ,idActual - i + 1,idActual)
		if (mejor_optimo == -1) or (mejor_optimo > optimo_calculado):
			mejor_optimo = optimo_calculado
			optimo_previo = idActual - i

	optimos[idActual] = mejor_optimo
	caminosOptimos[idActual] = optimo_previo
	return mejor_optimo

def recuperar_solucion_optima(cajas, caminosOptimos, alturasMaximas, n):
	if(n <= 0):
		return
	print(f"Altura Repisa:{altura_maxima(alturasMaximas, cajas, caminosOptimos[n] + 1, n)}" , end = '     ')
	for j in range(caminosOptimos[n] + 1,n + 1):
			print(f"C{cajas[j]}", end = ' ')
	print("\n//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n")
	recuperar_solucion_optima(cajas, caminosOptimos, alturasMaximas, caminosOptimos[n])

def main():
	cajas = []
	cajas.append(Caja(0,0,0))
	cajas = levantar_cajas_csv(cajas , argv[3])

	optimo_a_buscar = min(int(argv[1]), len(cajas) - 1)

	optimos, caminosOptimos, alturasMaximas = ordenadar_almacen(optimo_a_buscar, int(argv[2]), cajas)

	print("                     codigo caja:(altura caja / largo de caja) \n\n")

	recuperar_solucion_optima(cajas, caminosOptimos, alturasMaximas, optimo_a_buscar)
	print(f"\nla altura minima de las {optimo_a_buscar} cajas es : {optimos[optimo_a_buscar]}")

main()

