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
        edges.sort(key = itemgetter(2)) #Aqui se tiene que agregar el itemgetter para ordenar lo por peso antes no lo hacia
        for edge in edges:
            origin, destination, weight = edge
            #  String origin = edge[0];
            #  String destination = edge[1];
            #  int weigth = edge[2];
            if self.find_node(origin) != self.find_node(destination):
                self.validate_union(origin, destination)
                tree.append(edge)
        return tree

kruskal = Kruskal()
print('Ingrese los nodos separados por una coma')
nodes = input()
nodes = nodes.split(',')
print('Ingrese las conexion entre el nodo 1, 2 y peso separados por una coma para terminar ingrese un 0')
list_Aux = []
while True:
    inc = input()
    if inc.__eq__('0'):
        break
    list_Aux.append(inc.split(','))
kruskal = kruskal.kruskal(nodes,list_Aux)
print(*kruskal)

#[['0', '1', '4'], ['0', '7', '8'], ['1', '2', '8'], ['2', '3', '7'], ['2', '5', '4'], ['3', '4', '9'], ['6', '5', '2'], ['7', '8', '7']]
#7,6,1
#8,2,2
#6,5,2
#0,1,4
#2,5,4
#8,6,6
#2,3,7
#7,8,7
#0,7,8
#1,2,8
#3,4,9
#5,4,10
#1,7,11
#3,5,14