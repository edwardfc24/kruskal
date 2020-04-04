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
    # Fin Método Kruskal ---


    def __init__(self):
        self.nodes = {}
        self.order = {}
        self.loadInputs()


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
        edges.sort(key = itemgetter(2))
        for edge in edges:
            origin, destination, weight = edge
            #  String origin = edge[0];
            #  String destination = edge[1];
            #  int weigth = edge[2];
            if self.find_node(origin) != self.find_node(destination):
                self.validate_union(origin, destination)
                tree.append(edge)
        return tree

### Inicializar la clase kruskal y alimentar con datos ###
obj_kruskal = Kruskal()
# nodes = ['a', 'b', 'c', 'd' , 'e', 'f', 'g']
# edges = [['a', 'b', 7], ['a', 'd', 5], ['d', 'f', 6], ['b', 'e', 7], ['e', 'c', 5], ['e', 'g', 9]]
nodes = ['a','b','c','d','e','f','g','h','i','j','k','l']
edges = [['a','b',6],['a','c',6],['b','c',1],['a','d',6],['d','c',2],['b','e',2],['e','c',7],['e','f',4],['f','g',11],['c','g',2],['f','h',10],['h','g',22],['h','i',12],['i','g',2],['h','k',25],['i','k',16],['d','j',18],['i','j',1],['k','l',3],['j','l',8]]
tree = obj_kruskal.kruskal(nodes, edges)
print("El árbol obtenido es: ")
print(tree)
### Sumar los pesos del árbol resultante
path = 0
for edge in tree:
    path += edge[2]
print("El peso del árbol es: " + str(path))