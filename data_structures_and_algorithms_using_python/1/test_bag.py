#!/usr/bin/env python

import unittest
import bag

class Test(unittest.TestCase):

    def test_(self):
        self.b = bag.Bag()
        self.assertEquals(len(self.b),0)

    def test_add(self):
        self.test_()
        self.b.add(10000)
        self.assertEquals(len(self.b),1)
        self.b.add(5)
        self.assertEquals(len(self.b),2)

    def test_iterator(self):
        self.test_add()
        i = iter(self.b)
        self.assertEquals(next(i),10000)
        self.assertEquals(next(i),5)

    def test_iterator2(self):
        self.test_add()
        for i in self.b:
            self.assert_(i)

if __name__ == "__main__":
    unittest.main()
