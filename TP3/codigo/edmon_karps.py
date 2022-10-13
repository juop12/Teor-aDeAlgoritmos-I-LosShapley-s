#import bfs.py
from grafo_nuevo import *
#import pudb; pu.db

def bfs(grafo, verticeInicial):
    cola = [verticeInicial]
    visitados = [verticeInicial]

    proveniencia = {}
    while len(cola) > 0:
        vertice = cola.pop(0)
        print(vertice)

        for ady in grafo.adyacentes(vertice):
            if (ady not in visitados) and grafo.arista_peso(vertice, ady) != 0:
                cola.append(ady)
                visitados.append(ady)
                proveniencia[ady] = vertice
    return proveniencia

def encontrar_bottleneck(grafoResidual, camino, s, t):
    vertice_actual = t
    peso_actual = grafoResidual.arista_peso(camino[vertice_actual], vertice_actual)
    bottleneck = peso_actual
    while vertice_actual != s:
        peso_actual = grafoResidual.arista_peso(camino[vertice_actual], vertice_actual)
        bottleneck = min(bottleneck, peso_actual)
        vertice_actual = camino[vertice_actual]
    return bottleneck

def actualizar_arista(grafoResidual, inicio, fin, sumando):
    peso_actual = grafoResidual.arista_peso(inicio, fin)
    peso_modificado = peso_actual + sumando
    grafoResidual.insertar_arista(inicio, fin, peso_modificado)

def augment(grafoResidual, s, t):
    camino = bfs(grafoResidual, s)
    if t not in camino:
        return 0

    bottleneck = encontrar_bottleneck(grafoResidual, camino, s, t)

    vertice_actual = t 
    while vertice_actual != s:
        actualizar_arista(grafoResidual, camino[vertice_actual], vertice_actual, -1 * bottleneck)
        actualizar_arista(grafoResidual, vertice_actual, camino[vertice_actual], bottleneck)
        vertice_actual = camino[vertice_actual]
    
    return bottleneck

def construir_grafo_residual(grafo):
    vertices = grafo.obtener_vertices()
    for vertice in vertices:
        adyacentes = grafo.adyacentes(vertice)
        for ady in adyacentes:
            if not grafo.existe_arista(ady, vertice):
                grafo.insertar_arista(ady,vertice,0)

def edmond_karps(grafo, s, t):
    construir_grafo_residual(grafo)
    flujoNuevo = augment(grafo, s, t)
    flujoTotal = 0
    while flujoNuevo != 0:
        flujoTotal += flujoNuevo
        flujoNuevo = augment(grafo, s, t)
    return flujoTotal
    

def main():
    l = ['a','b','c','d','E1','E2']
    grafo = Grafo(l, True)

    grafo.insertar_arista('E1','a',53)
    grafo.insertar_arista('E1','b',63)
    grafo.insertar_arista('E1','c',52)
    grafo.insertar_arista('E1','d',51)
    
    grafo.insertar_arista('a','E2',64)
    grafo.insertar_arista('b','E2',51)
    grafo.insertar_arista('c','E2',64)
    grafo.insertar_arista('d','E2',64)

    grafo.insertar_arista('a','b',2)
    grafo.insertar_arista('b','a',2)
    grafo.insertar_arista('b','c',3)
    grafo.insertar_arista('c','b',3)
    grafo.insertar_arista('a','d',4)
    grafo.insertar_arista('d','a',4)

    yey = edmond_karps(grafo, 'E1', 'E2')
    print(yey)
        
main()
