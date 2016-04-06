'''
Created on Apr 5, 2016

@author: anishsingh1
'''

import MyDS

def HotPotato():
    people = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    num = 8
    
    q = MyDS.Queue()
    for n in people: q.enqueue(n)
        
    while q.size() > 1:
        for i in range(num):
            item = q.dequeue()
            q.enqueue(item)
        q.dequeue()
        
    print q.dequeue()
            
    

if __name__ == '__main__':
    HotPotato()