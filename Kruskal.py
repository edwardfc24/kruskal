from operator import itemgetter
class Kruskal:
    # Método Kruskal(Grafo)
    # Se inicializa el árbol de expansión mínima vacío                                                 
    # Se inicializa una estructura de unión-búsqueda                                                    
    # Se ordenan las aristas de menor a mayor peso                                                     
    #         Para cada arista a que une 2 vértices (u, v)
    #     Si u y v no están en la misma componente
    #             Se añade la arista a al árbol de expansión mínima. 
    #                         Se unen  las componentes de u y v
    #                 Fin Si
    # Fin Para
    # Fin Método Kruskal


    def __init__(self):
        self.nodes = {}
        self.order = {}


    def prepare_data(self, node):
        self.nodes[node] = node
        self.order[node] = 0


    def find_node(self, node):
        if self.nodes[node] != node:
            self.nodes[node] = self.find_node(self.nodes[node])
        return self.nodes[node]


    def validate_union(self, origin, destination):
        origin_auxiliar = self.find_node(origin)
        destination_auxiliar = self.find_node(destination)
        if origin_auxiliar != destination_auxiliar:
            if self.order[origin_auxiliar] > self.order[destination_auxiliar]:
                self.nodes[destination_auxiliar] = origin_auxiliar
            else:
                self.nodes[origin_auxiliar] = destination_auxiliar
                if self.order[origin_auxiliar] == self.order[destination_auxiliar]:
                    self.order[destination_auxiliar] += 1


    def kruskal(self, nodes, edges):
        # nodes ['a', 'b', 'c'.....]
        # edges ['origen', 'destino', entero]
        tree = []
        for node in nodes: 
            self.prepare_data(node)
        # Ordenar la lista
        edges = sorted(edges, key=itemgetter(2))
        for edge in edges:
            origin, destination, weight = edge
            #  String origin = edge[0];
            #  String destination = edge[1];
            #  int weigth = edge[2];
            if self.find_node(origin) != self.find_node(destination):
                self.validate_union(origin, destination)
                tree.append(edge)
        return tree


# nodes = ['a','b','c','d','e','f','g','h','i','j','k','l']
# edges = [['a','b',6],['a','c',6],['b','c',1],['a','d',6],['d','c',2],['b','e',2],['e','c',7],['e','f',4],['f','g',11],['c','g',2],['f','h',10],['h','g',22],['h','i',12],['i','g',2],['h','k',25],['i','k',16],['d','j',18],['i','j',1],['k','l',3],['j','l',8]]

# Proceso para pedir nodos
print('Ingresar cantidad de nodos')
cantidad = input()
while not cantidad.isnumeric():
    cantidad = input() 
nodos = []
cantidad = int(cantidad)
while cantidad > 0:
    nodos.append(input())
    cantidad = cantidad - 1

# Proceso para pedir aristas
print('Ingresar cantidad de aristas')
cantidad = input()
while not cantidad.isnumeric():
    cantidad = input()
print('Ingresar las aristas o edges en el siguiente formato: ')
print('ejemplo: a b 12')
cantidad = int(cantidad)
arista = []
while cantidad > 0:
    edge = input().strip().split(' ')
    if not len(edge) == 3:
        cantidad = cantidad + 1
    else:
        edge[2] = int(edge[2])
        arista.append(edge)
        cantidad = cantidad - 1

tree = Kruskal()
tree = tree.kruskal(nodos,arista)

suma = 0
for res in tree:
    print(str(res))
    suma = suma + int(res[2])
print(suma)


# Para correr el archivo en la consola en mi caso se coloca python3 Kruskal.py 
# Resultado
# ['b', 'c', 1]
# ['i', 'j', 1]
# ['b', 'e', 2]
# ['c', 'g', 2]
# ['d', 'c', 2]
# ['i', 'g', 2]
# ['k', 'l', 3]
# ['e', 'f', 4]
# ['a', 'b', 6]
# ['j', 'l', 8]
# ['f', 'h', 10]
# 41