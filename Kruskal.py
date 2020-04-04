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


    def loadInputs(self):
        print('Ingrese la lista de nodos: ')
        input_nodes = input()
        nodes_list = input_nodes.split(',')
        input_edges = ''
        end_key = 'cls'
        edge_list = []
        print('Ingrese las aristas: ')
        while input_edges.__ne__(end_key):
            input_edges = input()
            if(input_edges.__ne__(end_key)):
                aux_list = input_edges.split(',')
                weight = int(aux_list[2])
                aux_list[2] = weight
                edge_list.append(aux_list)
        print(self.kruskal(nodes_list, edge_list))
            


obj = Kruskal()
