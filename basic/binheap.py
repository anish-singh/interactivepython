'''
Created on Apr 9, 2016

@author: anishsingh1
'''

class BinaryHeap:
    '''
    classdocs
    '''
    
    def addItem(self, item):
        self.heap.append(item)
        self.last += 1
        self.moveUp(self.last)
        
        
    def moveUp(self, item_pos):
        
        while item_pos //2  > 0:
            if self.heap[item_pos // 2] > self.heap[item_pos]:
                self.heap[item_pos // 2], self.heap[item_pos] = self.heap[item_pos], self.heap[item_pos // 2]
                item_pos = item_pos // 2
            else: break
            

    def getItem(self):
        
        min = self.heap[1]
        self.heap[1] = self.heap[self.last]
        self.last -= 1
        self.heap.pop()
        self.moveDown(1)
        
        return min
    
    def moveDown(self, item_pos ):
        
        curr_pos = item_pos
        while curr_pos * 2 <= self.last :
            lc = curr_pos *2
            rc = lc + 1
            #compare with lc or rc and swap if lc or rc is less than item at curr_posn
            smaller_child_pos = lc
            if rc <= self.last  and self.heap[rc] < self.heap[lc]:
                smaller_child_pos = rc
            
            if self.heap[curr_pos] > self.heap[smaller_child_pos]:
                tmp = self.heap[curr_pos]
                self.heap[curr_pos] = self.heap[smaller_child_pos]
                self.heap[smaller_child_pos] = tmp
                curr_pos = smaller_child_pos
            else:
                break
                

    def __init__(self):
        self.heap = [0]
        self.last = 0
        
        '''
        Constructor
        '''
def main():
    b = BinaryHeap()
    #b.addItem(1)
    b.addItem(13)
    b.addItem(4)
    b.addItem(20)
    b.addItem(15)
    #b.addItem(0)
    print b.heap
    print b.getItem()
    print b.heap
    print b.getItem()
    print b.heap
if __name__ == '__main__':
    main()        