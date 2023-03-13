import timeit

start = timeit.default_timer()
#Grafo vacio
grafo = {'A':[('B',2),('D',6)],
         'B':[('A',2),('J',1),('C',2)],
         'C':[('B',2),('I',3),('F',1)],
         'D':[('A',6),('I',4),('M',3)],
         'J':[('B',1),('I',2)],
         'I':[('J',2),('C',3),('D',4),('H',2),('K',7)],
         'F':[('C',1),('G',2),('K',1)],
         'K':[('F',1),('G',4),('I',7)],
         'M':[('D',3),('N',5),('H',3)],
         'H':[('G',2),('I',2),('M',3),('N',3)],
         'G':[('F',2),('K',4),('L',2),('H',2)],
         'L':[('G',2),('N',1)],
         'N':[('H',3),('L',1),('M',5)]
         }

def dijkstra(grafo, inicial, final):
        INF = float('inf')
        sinVisitar = {nodo: INF for nodo in grafo.keys()}
        previo = {nodo: nodo for nodo in grafo.keys()} 
        visitado = {}
        actual = inicial
        pesoActual = 0
        sinVisitar[actual] = pesoActual

        while True:
            for nodo, peso in grafo[actual]:
                if nodo not in sinVisitar:
                    continue
                pesoNuevo = pesoActual + peso
                if sinVisitar[nodo] > pesoNuevo:
                    sinVisitar[nodo] = pesoNuevo
                    previo[nodo] = actual 
            visitado[actual] = pesoActual    
            sinVisitar.pop(actual)
            if not sinVisitar:
                break
            candidatos = [(n, s) for n, s in sinVisitar.items() if s != INF]
            actual, pesoActual = sorted(candidatos, key = lambda x: x[1])[0]
        camino = []
        nodo = final
        while True:
            camino.append(nodo)
            if(nodo == previo[nodo]):
                break
            nodo = previo[nodo]
        return (camino[::-1], visitado[final])

def nuevoArco(grafo, arco, peso):
        n1, n2 = tuple(arco)
        for n, e in [(n1, n2), (n2, n1)]:
            if n in grafo:
                if e not in grafo[n]:
                    grafo[n].append((e, peso))
                    if n == e:
                        break
            else:
                grafo[n] = [(e, peso)]

def tam(grafo):
        return len(grafo)

def prueba(grafo, inicial, final):

    ruta, pesoTotal = dijkstra(grafo, inicial, final)
    print(f'La ruta mas corta encontrada es:{ruta} peso:{pesoTotal}')

if __name__ == '__main__':

    inicial = 'A' 
    final = 'N'

    print(tam(grafo)+1)
    prueba(grafo, inicial, final)
    end = timeit.default_timer()
    print("Terminado en --- %s segundos ---" % (end - start))
    
    