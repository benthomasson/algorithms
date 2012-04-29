#!/usr/bin/env python
import unittest

def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
    return False

class Test(unittest.TestCase):

    def test_linearSearchTrue(self):
        self.assert_(linearSearch([1,2,3,4],3))

    def test_linearSearchFalse(self):
        self.assertFalse(linearSearch([1,2,3,4],5))

def sortedLinearSearch(theValues, item):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == item:
            return True
        elif theValues[i] > item:
            return False
    return False

class TestSorted(unittest.TestCase):

    def test_linearSearchTrue(self):
        self.assert_(sortedLinearSearch([1,2,3,4],3))

    def test_linearSearchFalse(self):
        self.assertFalse(sortedLinearSearch([1,2,3,4],5))
        self.assertFalse(sortedLinearSearch([1,2,3,4],0))

def findSmallest(theValues):
    n = len(theValues)
    smallest = theValues[0]
    for i in range(1,n):
        if theValues[i] < smallest:
            smallest = theValues[i]
    return smallest


class TestSmallest(unittest.TestCase):

    def test_linearSearchTrue(self):
        self.assertEquals(findSmallest([1,2,3,4]),1)

    def test_linearSearchFalse(self):
        self.assertEquals(findSmallest([5,1,3,4]),1)

if __name__ == "__main__":
    unittest.main()
