def bfs(grafo, verticeInicial):
    cola = [verticeInicial]
    visitados = [verticeInicial]

    while len(cola) > 0:
        vertice = cola.pop(0)
        #print(vertice)

        for ady in grafo.adyacencias(vertice):
            if ady not in visitados:
                cola.append(ady)
                visitados.append(ady)

