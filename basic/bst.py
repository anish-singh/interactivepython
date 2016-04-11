'''
Created on Apr 10, 2016

@author: anishsingh1
'''

class BST:
    '''
    classdocs
    '''
    def get(self, key):
        if not self.root: return None
        n = self.__get(key, self.root)
        return n.value
    
    
    def __get(self, key, node):
        
        if not node: return None
        elif node.key < key:
            return self.__get(key, node.left)
        elif node.key > key:
            return self.__get(key, node.right)
        elif     node.key == key:
            return node
        
    def put(self, key, value):
        if not self.root:
            self.root = Node(key, value)
            self.size += 1
        else:
            self.__put(self.root, key, value)
            
            
    def __put(self, node, key, value):
        
        if node.key < key:
            if not node.left:
                node.left = Node(key, value)
                self.size +=1 
            else:
                self.__put(node.left,key,value)
        elif node.key > key:
            if not node.right:
                node.right = Node(key, value)
                self.size +=1
            else:
                self.__put(node.right, key, value)
        elif node.key == key:
            node.value = value
            
            
            
                
            
            

    def __init__(self):
        self.root = None
        self.size = None
        
        '''
        Constructor
        '''
class Node:
    
    def __init__(self, key, value, parent = None, left = None, right = None): 
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        
    
           