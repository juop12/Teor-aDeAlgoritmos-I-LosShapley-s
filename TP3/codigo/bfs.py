from grafo import *
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



def main():
    l = ['a', 'b', 'c', 'd']
    grafo = Grafo(l, True)
    grafo.insertar_arista('a', 'b', 2)
    grafo.insertar_arista('a', 'd', 3)
    grafo.insertar_arista('b', 'c', 1)

    yey = bfs(grafo, 'a')
    print(yey)

main()