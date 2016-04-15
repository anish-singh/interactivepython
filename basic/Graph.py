'''
Created on Apr 13, 2016

@author: anishsingh1
'''

class Node:
    
    def __init__(self, data):
        self.data = data
        self.edges = {}
        
    def addEdge(self, toNode, weight):
        self.edges[toNode] = weight
    
    def getNeighbors(self):
        return self.edges.values()    
    

class Graph:
    
    def __init__(self):
        self.nodes = {}
        self.size = 0
        
    def addNode(self, nodeData):
        n = Node(nodeData)
        self[nodeData] = n
        self.size += 1
        return n
    
    def addEdge(self, fromNode, toNode, weight=0):
        if not self.nodes[fromNode]:
            self.addNode(fromNode)
        
        if not self.nodes[toNode]:
            self.addNode(toNode)
            
        self.nodes[fromNode].addEdge(toNode, weight)
        
    def __iter__(self):
        return iter(self.nodes.values())
    
    
    def getNode(self, nodeData):
        return self.nodes[nodeData]
    
    def getNodes(self):
        return self.nodes.values()
    
    
            