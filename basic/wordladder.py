'''
Created on Apr 14, 2016

@author: anishsingh1
'''

from basic.Graph import Graph
from basic.MyDS import Queue


def buildGraph(fileName):
    
    f = open(fileName,"rU")
    buckets = {}
    
    for line in f:
        word = line.strip()
        for i in range(len(word)):
            bucketName = word[:i] + '_' + word[i+1:]
            if not bucketName in buckets.keys():
                buckets[bucketName] = []
            if word not in buckets[bucketName]:
                    buckets[bucketName].append(word)
      
    # build graph
    g = Graph()
    
    for bucket in buckets.values():
        for w1 in bucket:
            for w2 in bucket:
                if w1 != w2:
                    g.addEdge(w1, w2)
    
    
    f.close()
    return g
    
    
def bfs(g, start):
    
    q = Queue()
    q.enqueue(start)
    while q.size() > 0:
        n = q.dequeue()
        n.status = 'VISITING'
        neighbors = n.getNeighbors()
        for i in neighbors:
            if i.status == 'NOT_VISITED':
                i.pred = n
                i.distance = n.distance +1
                q.enqueue(i)
        n.status = 'VISITED'
    
    
def getLadder(filename, startWord, endWord):
 
    g = buildGraph(filename)
    start = g.getNode(startWord)
    bfs(g, start)
    e = g.getNode(endWord)   
    while e:
        print e.getData()
        e = e.pred   
    
                
    
    

def main():
    getLadder("words.txt", 'hit', 'cog')

if __name__ == '__main__':
    main()