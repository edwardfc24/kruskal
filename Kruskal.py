class Kruskal:

# Comentario Inicial
    def __init__(self):
        self.nodes = {}
        self.order = {}

    def validate_data(self, node):
        self.nodes[node] = node
        self.order[node] = 0
