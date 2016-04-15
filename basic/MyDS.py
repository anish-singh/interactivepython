'''
Created on Apr 4, 2016

@author: anishsingh1
'''

class Stack:
    

    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if(self.items == []):
            raise Exception("Can't pop Empty Stack")
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []
    


class Queue:
    
    def __init__(self):
        self.q = []
    
    def enqueue(self, item):
        self.q.append(item)
        
    def dequeue(self):
        return self.q.pop(0)
        
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.q == []
    
    

class DeQueue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.insert(0,item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val
        
    def getNext(self):
        return self.next
    
    def setNext(self, n):
        self.next = n
        

    def size(self):
        count = 0
        n = self.head
        while n != None:
            count += 1
            n = n.getNext()
        return count
    
    def isEmpty(self):
        return self.head == None
    
class List:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def size(self):
        count = 0
        n = self.head
        while n != None:
            count += 1
            n = n.getNext()
        return count
    
    def isEmpty(self):
        return self.head == None


    def index(self, item):
        pass
    
    def pop(self):
        pass
    
    def append(self, item):
        pass
    
    def search(self, item):
        pass
    
    def remove(self, item):
        n = self.head
        prev = None
        
        while n != None:
            if n.getData() == item:
                #n is first node
                if prev == None:
                    self.head = n.getNext()
                else:
                    prev.setNext(n.getNext()) 
                
                return
            
            else:
                prev = n
                n = n.getNext()
    
    def add(self, item):
        pass
    
    def print_list(self):
        n = self.head
        while n != None:
            print n.getData()
            n = n.getNext()
        
    

class UnOrderedList (List):
    
    def __init__(self):
        List.__init__(self)
        
        
    def add(self, item):
        # add to front
        n = Node(item)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        
       
    def search(self, item):
        n = self.head
        while n != None:
            if n.getData() == item: return True
            n = n.getNext()
        return False
    
    
    def append(self, item):
         
        n = Node(item)
        
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.setNext(n)

  


class OrderedList(List):
    def __init__(self):
        List.__init__(self)
        
    def add(self, item):
        prev = None
        curr = self.head
        
        if self.head is None: 
            self.head = self.tail = Node(item)
        
        else:
            while curr != None:
                if curr.getData() > item :
                    n = Node(item)
                    if prev == None:
                        n.setNext(curr)
                        self.head = n
                    else:
                        n.setNext(curr)
                        prev.setNext(n)
                    break
                else:
                    prev = curr
                    curr = curr.getNext()
            else:
                n = Node(item)
                prev.setNext(n)
                
                
    
    def search(self, item):
        n = self.head
        while n != None:
            if(n.getData() < item): n=n.getNext()
            elif n.getData() == item: return True
            else: return False
        return False
            
        

    
def main():
    pass


if __name__ == '__main__':
    main()