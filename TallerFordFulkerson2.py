from sys import stdin

def primeraMatriz (lista, n):
    distancias = [[int(0)] * n for _ in range(n)]
    for fila in lista: 
        
        distancias[fila[0]][fila[1]]= fila [2]
    return distancias

def ford_fulkerson(matriz, fuente, sumidero):
    flujo_maximo = 0
    num_nodos = len(matriz)
    flujos = [[0] * num_nodos for _ in range(num_nodos)]
    
    while True:
        # Paso 2: Búsqueda de Caminos con (El metodo que quiera)
        camino, capacidad_minima = bfs(matriz, flujos, fuente, sumidero)
        if camino is None:
            break
        
        # Paso 3: Actualización del Flujo
        for i in range(len(camino) - 1):
            u, v = camino[i], camino[i + 1]
            flujos[u][v] += capacidad_minima
            flujos[v][u] -= capacidad_minima
        
        # Incrementamos el flujo máximo
        flujo_maximo += capacidad_minima
    
    # Paso 5: Resultado
    return flujo_maximo

def bfs(matriz, flujos, fuente, sumidero):
    num_nodos = len(matriz)
    cola = [fuente]
    caminos = {fuente: []}
    capacidades_minimas = {fuente: float('inf')}
    
    while cola:
        actual = cola.pop(0)
        
        for vecino in range(num_nodos):
            capacidad_residual = matriz[actual][vecino] - flujos[actual][vecino]
            if capacidad_residual > 0 and vecino not in caminos:
                capacidad_minima = min(capacidades_minimas[actual], capacidad_residual)
                caminos[vecino] = caminos[actual] + [actual]
                capacidades_minimas[vecino] = capacidad_minima
                
                if vecino == sumidero:
                    return caminos[vecino] + [sumidero], capacidad_minima
                
                cola.append(vecino)
                
    return None, 0

def dfs(matriz, flujos, fuente, sumidero):
    num_nodos = len(matriz)
    pila = [fuente]
    caminos = {fuente: []}
    capacidades_minimas = {fuente: float('inf')}
    
    while pila:
        actual = pila.pop()
        
        for vecino in range(num_nodos):
            capacidad_residual = matriz[actual][vecino] - flujos[actual][vecino]
            if capacidad_residual > 0 and vecino not in caminos:
                capacidad_minima = min(capacidades_minimas[actual], capacidad_residual)
                caminos[vecino] = caminos[actual] + [actual]
                capacidades_minimas[vecino] = capacidad_minima
                
                if vecino == sumidero:
                    return caminos[vecino] + [sumidero], capacidad_minima
                
                pila.append(vecino)
                
    return None, 0


def main():
    while True:
        n = stdin.readline().split()
        e = stdin.readline().split()
        if  len(n) == 0:
            break
        n= int(n[0])
        e= int(e[0])
        source = 0
        sink = n-1
        lista =[]   

        for _ in range(e): 
            a = list(map(int, input().split()))
            lista.append(a)
        lista = primeraMatriz (lista, n)

        print(ford_fulkerson(lista, source, sink))

if __name__ == '__main__':
    main()



