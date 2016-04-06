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
    
    
    
def main():
    None


if __name__ == '__main__':
    main()