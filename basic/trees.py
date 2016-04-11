'''
Created on Apr 9, 2016

@author: anishsingh1
'''

class BinaryTree:
    '''
    classdocs
    '''
    def __init__(self, data):
       
       self.data = data
       self.left = None
       self.right = None
       
    
    def addLeftChild(self, data):
        if self.left == None:
            self.left = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.left = self.left
            self.left = t
            
    def addRightChild(self, data):
        if self.right == None:
            self.right = BinaryTree(data)
        else:
            t = BinaryTree(data)
            t.right = self.right
            self.right = t
     
    def setValue(self, v):
        self.data = v
        
    def getValue(self):
        return self.data
    
    

def inorder(t):
    if t :
        inorder(t.left) 
        print t.getValue()
        inorder(t.right)
        
def preorder(t):
    if t:
        print t.getValue()
        preorder(t.left)
        preorder(t.right)
        
def postorder(t):
    if t:
        postorder(t.left)
        postorder(t.right)
        print t.getValue()