class Kruskal:
# Comentario Inicial
#david chavez villarroel estuvo aqui
    def __init__(self):
        self.nodes = {}
        self.order = {}
        
    #comentario 1

    def validate_data(self, node):
        self.nodes[node] = node
        self.order[node] = 0

