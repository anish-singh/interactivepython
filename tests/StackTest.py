'''
Created on Apr 4, 2016

@author: anishsingh1
'''
import unittest
from basic.MyDS import Stack


class Test(unittest.TestCase):

    s = Stack()

    def testPush(self):
        self.s.push(1)
        self.assertEqual(1, self.s.pop())
        
    def testEmpty(self):
        self.assertTrue(self.s.isEmpty(), "Empty Stack")
        
    def testError(self):
        try:
            self.s.pop()
        except Exception:
            self.assertTrue(True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPush']
    unittest.main()