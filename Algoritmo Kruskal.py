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
        edges.sort()
        for edge in edges:
            origin, destination, weight = edge
            #  String origin = edge[0];
            #  String destination = edge[1];
            #  int weigth = edge[2];
            if self.find_node(origin) != self.find_node(destination):
                self.validate_union(origin, destination)
                tree.append(edge)
        return tree

    def input(self):
        print("Ingrese los nodos: ")
        listaNodos = input()
        lista_nodos = listaNodos.split(',')
        print('Ingrese el origen, destino y peso separado por una coma')
        print('Coloque 0 para finalizar la entrada de datos')
        datos = ''
        lista_edges = []

        while datos.__ne__('0'):
            datos = input()

            if datos.__eq__('0'):
                break

            datos2 = datos.split(',')
            nuevo = int(datos2[2])
            datos2[2] = nuevo
            lista_edges.append(datos2)

        print(self.kruskal(lista_nodos, lista_edges))
        
        

# nodos = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# edges = ([
# ('A', 'B', 7),
# ('A', 'D', 5),
# ('B', 'A', 7),
# ('B', 'C', 8),
# ('B', 'D', 9),
# ('B', 'E', 7),
# ('C', 'B', 8),
# ('C', 'E', 5),
# ('D', 'A', 5),
# ('D', 'B', 9),
# ('D', 'E', 7),
# ('D', 'F', 6),
# ('E', 'B', 7),
# ('E', 'C', 5),
# ('E', 'D', 15),
# ('E', 'F', 8),
# ('E', 'G', 9),
# ('F', 'D', 6),
# ('F', 'E', 8),
# ('F', 'G', 11),
# ('G', 'E', 9),
# ('G', 'F', 11),
# ])

# Respuesta
# [['a', 'b', 7], ['a', 'd', 5], ['b', 'c', 8], ['b', 'e', 7], ['d', 'f', 6], ['e', 'g', 9]]


obj = Kruskal()
obj.input()
