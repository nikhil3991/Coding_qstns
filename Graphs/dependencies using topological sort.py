from collections import defaultdict

class Graph:
    def __init__(self):
        self.v =0
        self.nodes = []
        self.graph = defaultdict(list)

    def addNode(self,node):
        self.nodes.append(node)
        self.v+=1
        self.graph[node] = []

    def addEdge(self,u,v):
        self.graph[u].append(v)



projects = ['a','b','c','d','e','f','g']
dep = [['c','a'],['d','a'],['f','a'],['f','b'],['f','c'],['a','e'],['b','e'],['d','g']]
g= Graph()
for i in projects:
    g.addNode(i)
for i in dep:
    g.addEdge(i[1],i[0])
for i in g.graph:
    print(g.graph[i])






