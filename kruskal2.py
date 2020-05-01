class Kruskal:
    
    def __init__(self):
        self.nodes={}
        self.order={}

    def validatedata(self,node):
        self.nodes[node]=node
        self.order[node]=0
