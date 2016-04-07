'''
Created on Apr 6, 2016

@author: Medmeme1
'''
import unittest

from basic.MyDS import UnOrderedList
from basic.MyDS import OrderedList

class Test(unittest.TestCase):


    def testUnorderedList(self):
        mylist = UnOrderedList()

        mylist.add(31)
        mylist.add(77)
        mylist.add(17)
        mylist.add(93)
        mylist.add(26)
        mylist.add(54)
        
        self.assertEqual(mylist.size(),6)
        self.assertTrue(mylist.search(93))
        self.assertFalse(mylist.search(100))

        
        mylist.add(100)
        self.assertTrue(mylist.search(100))
        self.assertEqual(mylist.size(),7)
        
        mylist.remove(54)
        self.assertEqual(mylist.size(),6)
        mylist.remove(93)
        self.assertEqual(mylist.size(),5)
        mylist.remove(31)
        self.assertEqual(mylist.size(),4)
        self.assertFalse(mylist.search(93))

    def testOrderedList(self):
        mylist = OrderedList()
        mylist.add(31)
        mylist.add(77)
        mylist.add(17)
        mylist.add(93)
        mylist.add(26)
        mylist.add(54)
        
        self.assertEqual(mylist.size(),6)
        self.assertTrue(mylist.search(93))
        mylist.print_list()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testUnorderedList']
    unittest.main()