'''
Created on Apr 13, 2016

@author: anishsingh1
'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.edges = {}
        self.pred = None
        self.distance = 0
        self.status = 'NOT_VISITED'
        
    def addEdge(self, toNode, weight):
        self.edges[toNode] = weight
    
    def getNeighbors(self):
        return self.edges.keys()   
    
    def getData(self):
        return self.data 
    

class Graph:
    
    def __init__(self):
        self.nodes = {}
        self.size = 0
        
    def addNode(self, nodeData):
        n = Node(nodeData)
        self.nodes[nodeData] = n
        self.size += 1
        return n
    
    def addEdge(self, fromNode, toNode, weight=0):
        if fromNode not in self.nodes.keys():
            self.addNode(fromNode)
        
        if toNode not in self.nodes.keys():
            self.addNode(toNode)
            
        self.nodes[fromNode].addEdge(self.nodes[toNode], weight)
        
    def __iter__(self):
        return iter(self.nodes.values())
    
    
    def getNode(self, nodeData):
        return self.nodes[nodeData]
    
    def getNodes(self):
        return self.nodes.values()
    
    
            