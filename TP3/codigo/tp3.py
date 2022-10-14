from edmon_karps import edmond_karps
from grafo import Grafo
from csv import reader
from sys import argv
#import pudb; pu.db

EQUIPO1 = 'E1'
EQUIPO2 = 'E2'

def levantar_proyectos_csv(grafo, nombreDeArchivo):
	costosDeEquipo1 = {}
	costosDeEquipo2 = {}
	transferencias = {}
	sumaDePrecios = 0
	with open(nombreDeArchivo) as archivo:
		for linea in reader(archivo): 
			tarea = linea[0]
			costo_equipo1 = int(linea[1])
			costo_equipo2 = int(linea[2])
			
			grafo.insertar_vertice(tarea)
			sumaDePrecios += costo_equipo1 + costo_equipo2
			costosDeEquipo1[tarea] = costo_equipo1
			costosDeEquipo2[tarea] = costo_equipo2
			
			transferencias[tarea] = []
			for i in range(3,len(linea)-1,2):
				transferencias[tarea].append(linea[i])
				transferencias[tarea].append(int(linea[i+1]))
				
	return grafo, sumaDePrecios, costosDeEquipo1, costosDeEquipo2, transferencias

def insertar_deseabilidades(grafo, sumaDePrecios, costosDeEquipo1, costosDeEquipo2):
	for clave in costosDeEquipo1.keys():
		grafo.insertar_arista(EQUIPO1, clave, sumaDePrecios - costosDeEquipo2[clave])	
	for clave in costosDeEquipo2.keys():
		grafo.insertar_arista(clave, EQUIPO2, sumaDePrecios - costosDeEquipo1[clave])

def insertar_tansferencias(grafo, transferencias):
	for clave in transferencias:
		for i in range(0,len(transferencias[clave])-1,2):
			grafo.insertar_arista(clave, transferencias[clave][i], transferencias[clave][i+1])
			grafo.insertar_arista(transferencias[clave][i], clave, transferencias[clave][i+1])

def recuperar_resultados(grafoResidual, flujoMaximo, sumaDePrecios):
	tareasRealizadasPorElEquipo1 = []
	tareasRealizadasPorElEquipo2 = []

	for ady in grafoResidual.adyacentes(EQUIPO1):
		if grafoResidual.arista_peso(EQUIPO1, ady) == 0:
			tareasRealizadasPorElEquipo1.append(ady)
		else:
			tareasRealizadasPorElEquipo2.append(ady)
			
	precioMinimo = sumaDePrecios + (flujoMaximo - grafoResidual.cantidad_de_adyacentes(EQUIPO1) * sumaDePrecios)

	return tareasRealizadasPorElEquipo1, tareasRealizadasPorElEquipo2, precioMinimo
		
	
def main():
	ruta_archivo = argv[1]
	grafo = Grafo([EQUIPO1,EQUIPO2], True)
	grafo, sumaDePrecios, costosDeEquipo1, costosDeEquipo2, transferencias = levantar_proyectos_csv(grafo, ruta_archivo)
	
	insertar_deseabilidades(grafo, sumaDePrecios, costosDeEquipo1, costosDeEquipo2)
	insertar_tansferencias(grafo, transferencias)

	flujoMaximo = edmond_karps(grafo, EQUIPO1, EQUIPO2)

	tareasRealizadasPorElEquipo1, tareasRealizadasPorElEquipo2, precioMinimo = recuperar_resultados(grafo, flujoMaximo, sumaDePrecios)

	print("tareasRealizadasPorElEquipo1 ::", tareasRealizadasPorElEquipo1)
	print("tareasRealizadasPorElEquipo2 ::", tareasRealizadasPorElEquipo2)
	print("precioMinimo ::", precioMinimo)

main()

