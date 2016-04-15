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
            # print bucketName
            if not bucketName in buckets.keys():
                buckets[bucketName] = []
            if word not in buckets[bucketName]:
                    print 'adding word=%s to bucket %s' %(word, bucketName)
                    buckets[bucketName].append(word)
      
    # build graph
    g = Graph()
    for bucket in buckets.values():
        for w1 in bucket:
            for w2 in bucket:
                print w1 + ',' + w2
                if w1 != w2:
                    print 'adding edge %s, %s' %(w1,w2)
                    g.addEdge(w1, w2)
    
    
    f.close()
    return g
    
    
def bfs(g, key):
    start = g.getNode(key)
    q = Queue()
    q.enqueue(start)
    while q.size() > 0:
        n = q.dequeue()
        n.setStatus('VISITING')
        neighbors = n.getNeighbors()
        for i in neighbors:
            if i.getStatus() == 'NOT_VISITED':
                i.pred = n
                i.distance = n.distance +1
                q.enqueue(i)
        n.setStatus('VISITED')
    pass
    
    
def getLadder(filename, start, end):
   
    g = buildGraph(filename)
    bfs(g, start)
    e = g.getNode(end)   
    while e:
        print e.getData()
        e = e.pred()    
    
                
    
    

def main():
    getLadder("words.txt", 'hit', 'cog')

if __name__ == '__main__':
    main()