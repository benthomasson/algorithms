#!/usr/bin/env python

import unittest

import array

class Test(unittest.TestCase):

    def test_(self):
        self.a = array.Array(10)
        self.assertEquals(len(self.a),10)
        self.assertEquals(self.a[0],None)
        for i in self.a:
            self.assertEquals(i,None)

    def test_set(self):
        self.test_()
        self.a[3] = 10
        self.assertEquals(self.a[3],10)

    def test_iterator(self):
        self.test_()
        self.a[0] = 1
        self.a[1] = 2
        i = iter(self.a)
        self.assertEquals(next(i),1)
        self.assertEquals(next(i),2)



if __name__ == "__main__":
    unittest.main()
