'''
Created on Apr 13, 2016

@author: anishsingh1
'''

class Node:
    '''
    classdocs
    '''


    def __init__(self, data):
        self.data = data
        self.edges = {}
        
    def addEdge(self, e, weight = 0):
        self.edges[e] = weight
        
    def getEdges(self):
        return self.edges.keys()
    
    def getData(self):
        return self.data
    
    def getWeight(self, toNode):
        return self.edges[toNode]
    
    
        
class Graph:
    
    def __init__(self):
        self.numNodes = 0
        self.nodes = {}
        
    def addNode(self, key):
        n = Node(key)
        self.numNodes += 1
        self.nodes[key] = n
        return n
        
    def __contains__(self, n):
        return n in self.nodes
    
    def getNodes(self):
        return self.nodes.keys()
           
    
    def addEdge(self, toKey, frmKey, weight):
        if toKey not in self.nodes.keys():
            self.addNode(toKey)
        if frmKey not in self.nodes.keys():
            self.addNode(frmKey)
        self.nodes[frmKey].addEdge(self.nodes[toKey], weight)
        
    def __iter__(self):
        return iter(self.nodes.values())
            
  
    
        
    
        