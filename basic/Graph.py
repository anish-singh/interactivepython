'''
Created on Apr 13, 2016

@author: anishsingh1
'''

import unittest

class Node:
    
    def __init__(self, data):
        self.data = data
        self.edges = {}
        self.pred = None
        self.distance = 0
        self.status = 'NOT_VISITED'
        self.discovery = 0
        self.completed = 0
        
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
 
 
 
 
class DFSGraph(Graph):   
    
    def __init__(self):
        Graph.__init__(self)
        self.time = 0
        
        
    def dfs(self, n):
            self.time += 1
            if n.status == 'NOT_VISITED':
                n.discovery = self.time
                n.status = 'VISITING'
                print 'visiting %s discovery=%d, completed=%d' %(n.data, n.discovery, n.completed)
                for i in n.getNeighbors():
                    i.pred = n
                    self.dfs(i)
                n.status = 'VISITED'
                self.time += 1
                n.completed = self.time
                print 'visited %s discovery=%d, completed=%d' %(n.data, n.discovery, n.completed)

    def dfsForest(self):
        for n in self.getNodes():
            if n.status == 'NOT_VISITED':
                self.dfs(n)
            



class GraphTests:   
    def __init__(self):
        self.g = DFSGraph() 
        names = 'ABCDEF'
        for c in names:
            self.g.addNode(c)
        self.g.addEdge('A', 'B')
        self.g.addEdge('B', 'C')
        self.g.addEdge('B', 'D')
        self.g.addEdge('A', 'D')
        self.g.addEdge('D', 'E')
        self.g.addEdge('E', 'B')
        self.g.addEdge('E', 'F')
        self.g.addEdge('F', 'C')
     
    def testdfs(self):   
        self.g.dfsForest()


def main():
        t=GraphTests()
        t.testdfs()
    
if __name__ == '__main__':
    main()       
        
        
        
        
            