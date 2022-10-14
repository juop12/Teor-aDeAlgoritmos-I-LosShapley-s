from grafo import *
from cola import Cola
#import pudb; pu.db

def bfs(grafo, verticeInicial):
    cola = Cola()
    cola.encolar(verticeInicial)
    visitados = [verticeInicial]

    proveniencia = {}
    while cola.len() > 0:
        vertice = cola.desencolar()

        for ady in grafo.adyacentes(vertice):
            if (ady not in visitados) and grafo.arista_peso(vertice, ady) != 0:
                cola.encolar(ady)
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